from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

import web_pdb

class purchase_orders(Model):
	_name = 'purchase.orders'
	_description = 'Purchase Order'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_attrs = '_attrs_model_invisible'
	_date = 'doo'
	_rec_name = 'fullname'
	_columns = {
	'otype': fields.many2one(label='Type',obj='purchase.order.types',on_change='_on_change_otype', required = True),
	'name': fields.varchar(label = 'Name', required = True),
	'company': fields.many2one(label='Company',obj='md.company', required = True),
	'fullname': fields.composite(label='Full Name', cols = ['company','otype','name'], translate = True,required = True, compute = '_compute_composite'),
	'market_id': fields.many2one(label='Market',obj='purchase.markets'),
	'team_id': fields.many2one(label='Team',obj='purchase.teams'),
	'category_id': fields.many2one(label='Category',obj='purchase.order.categories'),
	'manager': fields.many2one(label='Manager',obj='bc.users'),
	'origin': fields.varchar(label = 'Origin'),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.date(label='Begin Date Of Order',required=True),
	'to_date': fields.date(label='End Date Of Order',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency',state={'approved':{'ro':True}}),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'pm': fields.selection(label='Price Method',selections=[('p','Plain'),('c','Complicated')]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','pur'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='purchase.order.items',rel='order_id'),
	'pricing': fields.one2many(label='Pricing',obj='purchase.order.pricing',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='purchase.order.roles',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='purchase.order.texts',rel='order_id'),
	'plates': fields.one2many(label='Plates',obj='purchase.order.output.plates',rel='order_id'),
	'payments': fields.one2many(label='Payments',obj='purchase.order.payment.schedules',rel='order_id'),
	'note': fields.text('Note',translate=True)
	}

	def _on_change_otype(self, item,context={}):		
		roles = self._pool.get('purchase.order.type.roles').select( ['role_id'],[('type_id','=',item['otype']['name'])],context)
		for role in roles:
			item_role = self._pool.get('purchase.order.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._pool.get('purchase.order.types').select( ['htschema'],[('name','=',item['otype']['name'])],context)	
		texts1 = self._pool.get('purchase.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = self._pool.get('purchase.order.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	def _on_change_bom(self, item,context={}):		
		#web_pdb.set_trace()
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = self._pool.get('md.bom.items').select( ['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = self._pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = self._pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None

	def _act_copy_to(self, column,record,context={}):				
		return 'Copy to'

	def _act_copy_from(self, column,record,context={}):				
		return 'Copy from'

	def _act_create_invoice(self, column,record,context={}):				
		return 'Create invoice'


	_actions = {
	'copy_to':{'label':'Copy To Model','tooltip':'Copy to other model','method':'_act_copy_to','icon':'add','view':['form']},
	'copy_from':{'label':'Copy From Model','tooltip':'Copy from other model','method':'_act_copy_from','icon':'list'},
	'create_invoice': {'label':'Creare Invice','tooltip':'Create Invoce From Order','method':'_act_create_invoice','icon':'shopping_cart'}
	}

	_default = {
		'state':'draft',
		'otype':'TA',
		'pm':'p'
	}

purchase_orders()

class purchase_order_texts(Model):
	_name = 'purchase.order.texts'
	_description = 'Purchase Order Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='purchase.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

purchase_order_texts()


class purchase_order_roles(Model):
	_name = 'purchase.order.roles'
	_description = 'Purchase Order Roles'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='purchase.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

purchase_order_roles()

class purchase_order_pricing(Model):
	_name = 'purchase.order.pricing'
	_description = 'Purchase Order Pricing'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='purchase.orders'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='purchase.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

purchase_order_pricing()

class purchase_order_payment_schedules(Model):
	_name = 'purchase.order.payment.schedules'
	_description = 'Purchase Order Payment Schedules'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='purchase.orders'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

purchase_order_payment_schedules()

class purchase_order_output_plates(Model):
	_name = 'purchase.order.output.plates'
	_description = 'Purchase Order Output Plates'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='purchase.orders'),
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

purchase_order_output_plates()

class purchase_order_items(Model):
	_name = 'purchase.order.items'
	_description = 'Purchase Order Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_hooks = {'aar':'_on_add_row'}
	_columns = {
	'order_id': fields.many2one(obj = 'purchase.orders',label = 'Purchase Order'),
	'itype_id': fields.many2one(label='Group Of Type Items', obj='md.type.items',domain=[('usage','in',('p','a'))]),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'volume': fields.float(label='Volume', readonly=True),
	'volume_total': fields.float(label='Volume Total', readonly=True),
	'volume_uom': fields.many2one(label="Volume UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Volume')]),
	'weight': fields.float(label='Weight', readonly=True),
	'weight_total': fields.float(label='Weight Total', readonly=True),
	'weight_uom': fields.many2one(label="Weight UoM",obj='md.uom', readonly=True,domain=[('quantity_id','=','Weight')]),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='purchase.order.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='purchase.order.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='purchase.order.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='purchase.order.item.texts',rel='item_id'),
	'plates': fields.one2many(label='Plates',obj='purchase.order.item.output.plates',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='purchase.order.item.payment.schedules',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_add_row(self,item,context={}):
		print('on_add_row:',item)
		pass

	def _attrs_model_invisible(self, item,context={}):
		if 'pm' in item and item['pm'] == 'c':
			return {'iv':{'price':True,'unit':True,'uop':True}}


	def _on_change_product(self, item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			i = self._pool.get('purchase.order.type.items').select( ['gti_id','itype_id'],[],context)
			gti = {}
			if len(i) > 0:
				for r in i:
					gti[r['gti_id']['name']] = r['itype_id']
			p = self._pool.get('md.product').select( ['name','gti','volume','volume_uom','weight','weight_uom',{'purchase':['vat','uom','price','currency','unit','uop']}],[('name','=',item['product']['name'])],context)
			if len(p) > 0:
				for f in ('gti','volume','volume_uom','weight','weight_uom','purchase'):
					if f == 'purchase':
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

	def _trgForEachRowBeforeInsertIB1(self, r1,context):
		print('Triger For Each Row Before Insert')

	def _trgForEachRowAfterInsertIA1(self, r1,context):
		print('Triger For Each Row After Insert')

	def _trgBeforeInsertIBA1(self, r1,context):
		print('Triger Before Insert')

	def _trgAfterInsertIAA1(self, r1,context):
		print('Triger After Insert')

#
	def _trgForEachRowBeforeUpdateUB1(self, r1,r2,context):
		print('Triger For Each Row Before Update')

	def _trgForEachRowAfterUpdateUA1(self, r1,r2,context):
		print('Triger For Each Row After Update')

	def _trgBeforeUpdateUBA1(self, r1,r2,context):
		print('Triger Before Update')

	def _trgAfterUpdateIUA1(self, r1,r2,context):
		print('Triger After Update')
#
	def _trgForEachRowBeforeDeleteDB1(self, r2,context):
		print('Triger For Each Row Before Delete')

	def _trgForEachRowAfterDeleteDA1(self, r2,context):
		print('Triger For Each Row After Delete')

	def _trgBeforeDeleteDBA1(self, r2,context):
		print('Triger Before Delete')

	def _trgAfterDeleteDA1(self, r2,context):
		print('Triger After Delete')



	_default = {
		'unit': 1
	}

purchase_order_items()

class purchase_order_pricing_items(Model):
	_name = 'purchase.order.pricing.items'
	_description = 'Purchase Order Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='purchase.order.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='purchase.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

purchase_order_pricing_items()

class purchase_order_item_texts(Model):
	_name = 'purchase.order.item.texts'
	_description = 'Purchase Order Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='purchase.order.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

purchase_order_item_texts()


class purchase_order_item_roles(Model):
	_name = 'purchase.order.item.roles'
	_description = 'Purchase Order Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='purchase.order.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

purchase_order_item_roles()

class purchase_order_item_delivery_schedules(Model):
	_name = 'purchase.order.item.delivery.schedules'
	_description = 'Purchase Order Item Delivery Schedules'
	_matrix_names = ('schedule','quantity')
	_columns = {
	'item_id': fields.many2one(obj = 'purchase.order.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

purchase_order_item_delivery_schedules()

class purchase_order_item_output_plates(Model):
	_name = 'purchase.order.item.output.plates'
	_description = 'Purchase Order Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='purchase.order.items'),
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

purchase_order_item_output_plates()

class purchase_order_item_payment_schedules(Model):
	_name = 'purchase.order.item.payment.schedules'
	_description = 'Purchase Order Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='purchase.order.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

purchase_order_item_payment_schedules()

# Invoice
class purchase_invoices(Model):
	_name = 'purchase.invoices'
	_description = 'Purchase Invoice'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doi'
	_rec_name = 'fullname'
	_columns = {
	'itype': fields.many2one(label='Type',obj='purchase.invoice.types',on_change='on_change_itype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols = ['company','itype','name'], translate = True,required = True, compute = '_compute_composite'),
	'market_id': fields.many2one(label='Market',obj='purchase.markets'),
	'team_id': fields.many2one(label='Team',obj='purchase.teams'),
	'category_id': fields.many2one(label='Category',obj='purchase.invoce.categories'),
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
	'bom': fields.many2one(label='BoM',obj='md.boms',domain=[('usage','=','pur'),'|',('usage','=','all')],on_change='_on_change_bom'),
	'items': fields.one2many(label='Items',obj='purchase.invoice.items',rel='invoice_id'),
	'pricing': fields.one2many(label='Pricing',obj='purchase.invoice.pricing',rel='invoice_id'),
	'roles': fields.one2many(label='Roles',obj='purchase.invoice.roles',rel='invoice_id'),
	'texts': fields.one2many(label='Texts',obj='purchase.invoice.texts',rel='invoice_id'),
	'note': fields.text('Note')
	}

	def _on_change_itype(self, item,context={}):		
			roles = self._pool.get('purchase.invoice.type.roles').select(['role_id'],[('type_id','=',item['otype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	def _on_change_bom(self, item,context={}):		
		if item['bom'] and 'name' in item['bom'] and item['bom']['name']:
			p = self._pool.get('md.bom.input.items').select( ['product','quantity','uom'],[('bom_id','=',item['bom']['name'])],context)
			for i in p:
				ei = self._pool.get('purchase.order.item.delivery.schedules')._buildEmptyItem()
				ei['quantity'] = i['quantity']
				ei['schedule'] = datetime.now().astimezone()+timedelta(3)
				item_items = self._pool.get('purchase.order.items')._buildEmptyItem()
				item_items['delivery_schedules'].append(ei)
				for f in ('product','uom'):
					item_items[f] = i[f]
				item_items['price'] = 0.00
				item['items'].append(item_items)

		return None



	_default = {
		'state':'draft',
		'itype':'in'
	}

purchase_invoices()

class purchase_invoice_pricing(Model):
	_name = 'purchase.invoice.pricing'
	_description = 'Purchase Invoice Pricing'
	_columns = {
	'invoice_id': fields.many2one(label = 'Invoice',obj='purchase.invoices'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='purchase.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

purchase_invoice_pricing()

class purchase_invoice_texts(Model):
	_name = 'purchase.invoice.texts'
	_description = 'Purchase Invoce Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'invoice_id': fields.many2one(label='Order',obj='purchase.invoices'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

purchase_invoice_texts()


class purchase_invoice_roles(Model):
	_name = 'purchase.invoice.roles'
	_description = 'Purchase Invoice Roles'
	_columns = {
	'invoice_id': fields.many2one(label = 'Invoice',obj='purchase.invoices'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

purchase_invoice_roles()

class purchase_invoice_items(Model):
	_name = 'purchase.invoice.items'
	_description = 'Purchase Invoice Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'invoice_id': fields.many2one(obj = 'purchase.invoices',label = 'Invoice'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='purchase.invoce.item.delivery.schedules',rel='item_id'),
	'pricing': fields.one2many(label='Pricing',obj='purchase.invoice.pricing.items',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='purchase.invoice.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='purchase.invoice.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self, item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self._pool.get('md.purchase.product').select( ['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

purchase_invoice_items()

class purchase_invoice_item_texts(Model):
	_name = 'purchase.invoice.item.texts'
	_description = 'Purchase Invoce Item Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='purchase.invoice.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='purchase.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

purchase_invoice_item_texts()


class purchase_invoice_item_roles(Model):
	_name = 'purchase.invoice.item.roles'
	_description = 'Purchase Invoice Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='purchase.invoice.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

purchase_invoice_item_roles()

class purchase_invoice_pricing_items(Model):
	_name = 'purchase.invoice.pricing.items'
	_description = 'Purchase Invoice Item Pricing'
	_columns = {
	'item_id': fields.many2one(label = 'Order',obj='purchase.invoice.items'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','p')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='purchase.pricing.group.levels'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'cop': fields.many2one(label='Currency Of Price',obj='md.currency',required=True),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

purchase_invoice_pricing_items()


class purchase_invoce_item_delivery_schedules(Model):
	_name = 'purchase.invoce.item.delivery.schedules'
	_description = 'Purchase Invoice Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'purchase.invoice.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

purchase_invoce_item_delivery_schedules()

# inherit

class md_purchase_product(Model):
	_name = 'md.purchase.product'
	_description = 'Purchase Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'vat': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_purchase_product()

class md_purchase_product_inherit(ModelInherit):
	_name = 'md.purchase.product.inherit'
	_description = 'Genaral Model Inherit For Purchase Product'
	_inherit = {'md.product':{'_columns':['purchase']},'md.boms':{'_columns':['usage']},'seq.conditions':{'_columns':['usage']},'seq.access.schemas':{'_columns':['usage']},'seq.access':{'_columns':['usage']},'md.type.items':{'_columns':['usage']},'md.type.plates':{'_columns':['usage']}}
	_columns = {
		'purchase': fields.one2many(label='Purchase',obj='md.purchase.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('pur','Purchase')])
	}
	
md_purchase_product_inherit()
