from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

class sale_orders(Model):
	_name = 'sale.orders'
	_description = 'Sale Orders'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_rec_name = 'fullname'
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='sale.order.types',on_change='_on_change_otype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','otype','name'], translate = True,required = True),
	'market': fields.many2one(label='Market',obj='sale.markets'),
	'team': fields.many2one(label='Team',obj='sale.teams'),
	'category_id': fields.many2one(label='Category',obj='sale.order.categories'),
	'origin': fields.varchar(label = 'Origin'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.date(label='Begin Date Of Order',required=True),
	'to_date': fields.date(label='End Date Of Order',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'mob': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','sale'),'|',('usage','=','all')],on_change='_on_change_mob'),
	'items': fields.one2many(label='Items',obj='sale.order.items',rel='order_id'),
	'pricing': fields.one2many(label='Pricing',obj='sale.order.pricing',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='sale.order.roles',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='sale.order.texts',rel='order_id'),
	'plates': fields.one2many(label='Plates',obj='sale.order.output.plates',rel='order_id'),
	'payments': fields.one2many(label='Payments',obj='sale.order.payment.schedules',rel='order_id'),
	'note': fields.text('Note')
	}

	def _on_change_otype(self ,item,context={}):		
		roles = self._proxy.get('sale.order.type.roles').select(['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = self._proxy.get('sale.order.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._proxy.get('sale.order.types').select( ['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = self._proxy.get('sale.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		if len(texts1) > 0:
			texts = texts1[0]['texts']
			seq = 0
			for text in texts:
				item_text = self._proxy.get('sale.order.texts')._buildEmptyItem()
				if text['seq']:
					item_text['seq'] = text['seq']
				else:
					item_text['seq'] = seq
					seq += 10
				item_text['text_id'] = text['text_id']
				item['texts'].append(item_text)

	def _on_change_mob(self ,item,context={}):		
		if item['mob'] and 'name' in item['mob'] and item['mob']['name']:
			p = self._proxy.get('md.mob.output.items').select( ['product','quantity','uom'],[('mob_id','=',item['mob']['name'])],context)
			for i in p:
				ei = self._proxy.get('sale.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = self._proxy.get('sale.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

#

	_default = {
		'state':'draft'
	}

sale_orders()

class sale_order_texts(Model):
	_name = 'sale.order.texts'
	_description = 'Sale Order Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='sale.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_order_texts()

class sale_order_roles(Model):
	_name = 'sale.order.roles'
	_description = 'Sale Order Roles'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_order_roles()

class sale_order_pricing(Model):
	_name = 'sale.order.pricing'
	_description = 'Sale Order Pricing'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='sale.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

sale_order_pricing()

class sale_order_payment_schedules(Model):
	_name = 'sale.order.payment.schedules'
	_description = 'Sale Order Payment Schedules'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

sale_order_payment_schedules()

class sale_order_output_plates(Model):
	_name = 'sale.order.output.plates'
	_description = 'Sale Order Output Plates'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('iscustomer',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('c','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

sale_order_output_plates()

class sale_order_items(Model):
	_name = 'sale.order.items'
	_description = 'Sale Order Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'order_id': fields.many2one(obj = 'sale.orders',label = 'Sales Order'),
	'itype_id': fields.many2one(label='Group Of Type Items', obj='md.type.items',domain=[('usage','in',('s','a'))]),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'volume': fields.float(label='Volume', readonly=True),
	'volume_total': fields.float(label='Volume Total', readonly=True),
	'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Volume')]),
	'weight': fields.float(label='Weight', readonly=True),
	'weight_total': fields.float(label='Weight Total', readonly=True),
	'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Weight')]),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='sale.order.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='sale.order.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='sale.order.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='sale.order.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='sale.order.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='sale.order.item.payment.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self ,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			i = self._proxy.get('sale.order.type.items').select( ['gti_id','itype_id'],[],context)
			gti = {}
			if len(i) > 0:
				for r in i:
					gti[r['gti_id']['name']] = r['itype_id']
			p = self._proxy.get('md.product').select( ['name','gti','volume','volume_uom','weight','weight_uom',{'sale':['vat','uom','price','currency','unit','uop']}],[('name','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('gti','volume','volume_uom','weight','weight_uom','sale'):
					if f == 'sale':
						if len(p[0][f]) > 0:
							d = p[0][f][0]
							for m in ('uom','price','currency','unit','uop','vat'):
								if m not in item or item[m] != d[m]:
									if m == 'vat':
										item['vat_code'] = d['vat']				
									else:
										item[m] = d[m]
					else:
						if f == 'gti':
							if p[0]['gti']['name'] in gti:
								item['itype_id'] = gti[p[0][f]['name']]
						else:
							if f not in item or item[f] != p[0][f]:
								item[f] = p[0][f]

			else:
				for f in ('vat_code','uom','price','currency','unit','uop'):
					if f in ('price','unit'):
						if f in self._default:
							item[f] = self._default[f]
						else:
							item[f] = None
					else:
						item[f] = {'id':None,'name':None}

		return None

	_trg_upd_cols = ['product','guantity','amount']

	_trigers = {
		'bir': '_trgForEachRowBeforeInsertIB1',
		'bur': '_trgForEachRowBeforeUpdateUB1',
		'bdr': '_trgForEachRowBeforeDeleteDB1',
		'air': '_trgForEachRowAfterInsertIA1',
		'aur': '_trgForEachRowAfterUpdateUA1',
		'adr': '_trgForEachRowAfterDeleteDA1',
		'bi': '_trgBeforeInsertIBA1',
		'bu': '_trgBeforeUpdateUBA1',
		'bd': '_trgBeforeDeleteDBA1',
		'ai': '_trgBeforeInsertIBA1',
		'au': '_trgAfterUpdateIUA1',
		'ad': '_trgAfterDeleteDA1',
		}

	def _trgForEachRowBeforeInsertIB1(self ,r1,context):
		print('Triger For Each Row Before Insert')

	def _trgForEachRowAfterInsertIA1(self ,r1,context):
		print('Triger For Each Row After Insert')

	def _trgBeforeInsertIBA1(self ,r1,context):
		print('Triger Before Insert')

	def _trgAfterInsertIAA1(self ,r1,context):
		print('Triger After Insert')

#
	def _trgForEachRowBeforeUpdateUB1(self ,r1,r2,context):
		print('Triger For Each Row Before Update')

	def _trgForEachRowAfterUpdateUA1(self ,r1,r2,context):
		print('Triger For Each Row After Update')

	def _trgBeforeUpdateUBA1(self ,r1,r2,context):
		print('Triger Before Update')

	def _trgAfterUpdateIUA1(self ,r1,r2,context):
		print('Triger After Update')
#
	def _trgForEachRowBeforeDeleteDB1(self ,r2,context):
		print('Triger For Each Row Before Delete')

	def _trgForEachRowAfterDeleteDA1(self ,r2,context):
		print('Triger For Each Row After Delete')

	def _trgBeforeDeleteDBA1(self ,r2,context):
		print('Triger Before Delete')

	def _trgAfterDeleteDA1(self ,r2,context):
		print('Triger After Delete')

	_default = {
		'quantity': 1,
		'unit': 1
	}

sale_order_items()

class sale_order_pricing_items(Model):
	_name = 'sale.order.pricing.items'
	_description = 'Sale Order Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Order',obj='sale.order.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='sale.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

sale_order_pricing_items()

class sale_order_item_texts(Model):
	_name = 'sale.order.item.texts'
	_description = 'Sale Order Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='sale.order.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_order_item_texts()


class sale_order_item_roles(Model):
	_name = 'sale.order.item.roles'
	_description = 'Sale Order Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.order.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_order_item_roles()


class sale_order_item_delivery_schedules(Model):
	_name = 'sale.order.item.delivery.schedules'
	_description = 'Sales Order Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'sale.order.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

sale_order_item_delivery_schedules()

class sale_order_item_output_plates(Model):
	_name = 'sale.order.item.output.plates'
	_description = 'Sale Order Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Order',obj='sale.order.items'),
	'state': fields.selection(label='State',selections=[('c','Created'),('p','Printed'),('e','Error'),('w','Warning'),('i','Info')],required=True),
	'otype': fields.many2one(label='Type',obj='md.type.plates',required=True,domain=[('usage','=','p'),'|',('usage','=','a')]),
	'partner': fields.many2one(label='Partner',obj='md.partner',required=True,domain=[('issuplier',)]),
	'role': fields.many2one(label = 'Role',obj='md.role.partners',required=True,domain=[('trole','in',('s','i','p','a'))]),
	'language': fields.many2one(label = 'language',obj='md.language',required=True),
	'msm': fields.selection(label='Message Sending Method',selections=[('pj','Peridiocal Job Send'),('tj','Timing Job Send'),('ss','Self Output Send'),('im','Immediately Send')],required=True),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'c'
	}

sale_order_item_output_plates()

class sale_order_item_payment_schedules(Model):
	_name = 'sale.order.item.payment.schedules'
	_description = 'Sale Order Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.order.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

sale_order_item_payment_schedules()

# Invoice
class sale_invoices(Model):
	_name = 'sale.invoices'
	_description = 'Sale Invoices'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doi'
	_columns = {
	'itype': fields.many2one(label='Type',obj='sale.invoice.types',on_change='on_change_itype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','itype','name'], translate = True,required = True),
	'market_id': fields.many2one(label='Market',obj='sale.markets'),
	'team_id': fields.many2one(label='Team',obj='sale.teams'),
	'category_id': fields.many2one(label='Category',obj='sale.invoice.categories'),
	'origin': fields.varchar(label = 'Origin'),
	'doi': fields.date(label='Date Of Invoice',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'items': fields.one2many(label='Items',obj='sale.invoice.items',rel='invoice_id'),
	'roles': fields.one2many(label='Roles',obj='sale.invoice.roles',rel='invoice_id'),
	'texts': fields.one2many(label='Texts',obj='sale.invoice.texts',rel='invoice_id'),
	'note': fields.text('Note')
	}

	def _on_change_itype(self ,item,context={}):		
			roles = self._proxy.get('sale.invoice.type.roles').select(['role_id'],[('type_id','=',item['otype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]


	_default = {
		'state':'draft'
	}

sale_invoices()

class sale_invoice_texts(Model):
	_name = 'sale.invoice.texts'
	_description = 'Sale Invoce Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'invoice_id': fields.many2one(label='Order',obj='sale.invoices'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_invoice_texts()

class sale_invoice_roles(Model):
	_name = 'sale.invoice.roles'
	_description = 'sale Invoice Roles'
	_columns = {
	'invoice_id': fields.many2one(label = 'Invoice',obj='sale.invoices'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_invoice_roles()

class sales_invoice_items(Model):
	_name = 'sale.invoice.items'
	_description = 'Sales Invoice Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'invoice_id': fields.many2one(obj = 'sale.invoices',label = 'Invoice'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'	),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='sale.invoice.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='sale.invoice.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='sale.invoice.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self ,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self._proxy.get('md.sale.product').select(['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

sales_invoice_items()

class sale_invoice_item_texts(Model):
	_name = 'sale.invoice.item.texts'
	_description = 'Sale Invoce Item Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Order',obj='sale.invoice.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_invoice_item_texts()

class sale_invoice_item_roles(Model):
	_name = 'sale.invoice.item.roles'
	_description = 'Sale Invoice Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.invoice.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_invoice_item_roles()

class sales_invoce_item_delivery_schedules(Model):
	_name = 'sale.invoice.item.delivery.schedules'
	_description = 'Sales Order Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'sale.invoice.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

sales_invoce_item_delivery_schedules()

#inherit

class md_sale_product(Model):
	_name = 'md.sale.product'
	_description = 'Sale Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'vat': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_sale_product()

class md_sale_product_inherit(ModelInherit):
	_name = 'md.sale.product.inherit'
	_description = 'Genaral Model Inherit For Sale Product'
	_inherit = {'md.product':{'_columns':['sale']},'md.mobs':{'_columns':['usage']},'md.type.items':{'_columns':['usage']},'seq.conditions':{'_columns':['usage']},'seq.access.schemas':{'_columns':['usage']},'seq.access':{'_columns':['usage']}}
	_columns = {
		'sale': fields.one2many(label='Sales',obj='md.sale.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('sale','Sale')])
	}
	
md_sale_product_inherit()

