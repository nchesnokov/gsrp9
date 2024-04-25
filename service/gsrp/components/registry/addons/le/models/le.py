from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

from decimal import Decimal


class md_pack_product(Model):
	_name = 'md.pack.product'
	_description = 'Pack Of Product'
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

md_pack_product()


class md_pack_product_inherit(ModelInherit):
	_name = 'md.pack.product.inherit'
	_description = 'Genaral Model Inherit For project Product'
	_inherit = {'md.product':{'_columns':['pack']},'md.boms':{'_columns':['usage']}}
	_columns = {
		'pack': fields.one2many(label='Pack',obj='md.pack.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('pack','Pack')])
	}
	
md_pack_product_inherit()

# Inbound Delivery
class le_inbound_delivery(Model):
	_name = 'le.inbound.delivery'
	_description = 'Inbound Delivery'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',required = True,obj='le.inbound.delivery.types',on_change='_on_change_dtype'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'point_id': fields.related(label='Shipping Point',obj='le.shipping.points',relatedy=['company_id'],domain=[('ptype','in',('i','b'))]),
	'place_id': fields.related(label='Loading Place',obj='le.loading.places',relatedy=['point_id']),
	'category_id': fields.many2one(label='Category',obj='le.inbound.delivery.category'),
	'name': fields.varchar(label = 'Name'),
	'origin': fields.varchar(label = 'Origin'),
	'dod': fields.date(label='Date Of Delivery',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	#'pricing': fields.one2many(label='Pricing',obj='le.inbound.delivery.pricing',rel='order_id'),
	'items': fields.one2many(label='Items',obj='le.inbound.delivery.items',rel='delivery_id'),
	'roles': fields.one2many(label='Roles',obj='le.inbound.delivery.roles',rel='delivery_id'),
	'texts': fields.one2many(label='Texts',obj='le.inbound.delivery.texts',rel='delivery_id'),
	#'payments': fields.one2many(label='Payments',obj='le.inbound.delivery.payment.schedules',rel='delivery_id'),
	#'plates': fields.one2many(label='Plates',obj='le.inbound.delivery.output.plates',rel='delivery_id'),
	'note': fields.text('Note')
	}

	def _on_change_dtype(self,item,context={}):		
		roles = self._proxy.get('le.inbound.delivery.type.roles').select( ['role_id'],[('type_id','=',item['dtype']['name'])],context)
		for role in roles:
			item_role = self._proxy.get('le.inbound.delivery.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._proxy.get('le.inbound.delivery.types').select( ['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = self._proxy.get('le.delivery.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = self._proxy.get('le.inbound.delivery.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	_default = {
		'state':'draft'
	}

le_inbound_delivery()

class le_inbound_delivery_texts(Model):
	_name = 'le.inbound.delivery.texts'
	_description = 'Inbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'delivery_id': fields.many2one(label='Delivery',obj='le.inbound.delivery'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_inbound_delivery_texts()

class le_inbound_delivery_roles(Model):
	_name = 'le.inbound.delivery.roles'
	_description = 'Inbound Delivery Roles'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.inbound.delivery'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

le_inbound_delivery_roles()

class le_inbound_delivery_pricing(Model):
	_name = 'le.inbound.delivery.pricing'
	_description = 'Inbound Delivery Pricing'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.inbound.delivery'),
	'level': fields.integer(label = 'Level'),
	'cond': fields.many2one(label='Condition',obj='seq.conditions',domain=[('area','=','b'),('usage','=','s')],required=True),
	'from_level': fields.integer(label = 'From Level'),
	'to_level': fields.integer(label = 'To Level'),
	'group_level': fields.many2one(label = 'Group Level',obj='le.pricing.group.levels'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency',required=True),
	}

le_inbound_delivery_pricing()

class le_inbound_delivery_payment_schedules(Model):
	_name = 'le.inbound.delivery.payment.schedules'
	_description = 'Inbound Delivery Payment Schedules'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.inbound.delivery'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

le_inbound_delivery_payment_schedules()

class le_inbound_delivery_items(Model):
	_name = 'le.inbound.delivery.items'
	_description = 'Inbound Delivery Items'
	_columns = {
	'delivery_id': fields.many2one(obj = 'le.inbound.delivery',label = 'Delivery'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'packlist': fields.one2many(label='Pack List',obj='le.inbound.delivery.packlist',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='le.inbound.delivery.item.texts',rel='item_id'),
	#'plates': fields.one2many(label='Plates',obj='le.inbound.delivery.item.output.plates',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _calculate_items(self,item,context={}):		
		if item['quantity'] and item['price'] and item['unit']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = self._proxy.get('md.vat.code').read(ids,['value','subtype_vat'],context)[0]
				v = r['value']
				s = r['subtype_vat']
				if s == 'e':
					item['vat_amount'] = item['amount'] * Decimal('0.%s' % (v,)) 
				elif s == 'i':
					item['vat_amount'] = item['amount'] - item['amount'] * Decimal('0.%s' % (v,)) 

		if 'amount' in item and item['amount']:
			item['total_amount'] = item['amount']
			if 'vat_amount' in item:
				if item['vat_amount']:
					item['total_amount'] += item['vat_amount'] 

		return None

	def _on_change_product(self,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self._proxy.get('md.purchase.product').select(['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

le_inbound_delivery_items()

class le_inbound_delivery_output_plates(Model):
	_name = 'le.inbound.delivery.output.plates'
	_description = 'Inbound Delivery Output Plates'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.inbound.delivery'),
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

le_inbound_delivery_output_plates()


class le_inbound_delivery_item_texts(Model):
	_name = 'le.inbound.delivery.item.texts'
	_description = 'Inbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='le.inbound.delivery.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_inbound_delivery_item_texts()

class le_inbound_delivery_item_output_plates(Model):
	_name = 'le.inbound.delivery.item.output.plates'
	_description = 'Inbound Delivery Item Output Plates'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='le.inbound.delivery.items'),
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

le_inbound_delivery_item_output_plates()



class le_inbound_delivery_packlist(Model):
	_name = 'le.inbound.delivery.packlist'
	_description = 'Packlist Of Inbound Delivery'
	_columns = {
	'item_id': fields.many2one(obj = 'le.inbound.delivery.items',label = 'Delivery Item'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'note': fields.text(label = 'Note')
	}

	def _calculate_items(self,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = self._proxy.get('md.vat.code').read(ids,['value','subtype_vat'],context)[0]
				v = r['value']
				s = r['subtype_vat']
				if s == 'e':
					item['vat_amount'] = item['amount'] * Decimal('0.%s' % (v,)) 
				elif s == 'i':
					item['vat_amount'] = item['amount'] - item['amount'] * Decimal('0.%s' % (v,)) 

		if 'amount' in item and item['amount']:
			item['total_amount'] = item['amount']
			if 'vat_amount' in item:
				if item['vat_amount']:
					item['total_amount'] += item['vat_amount'] 

		return None

	def _on_change_product(self,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self._proxy.get('md.purchase.product').select(['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit':1
	}

le_inbound_delivery_packlist()
# Inbound Delivery end
class le_outbound_delivery(Model):
	_name = 'le.outbound.delivery'
	_description = 'Outbound Delivery'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dod'
	_columns = {

	'dtype': fields.many2one(label='Type',required = True,obj='le.inbound.delivery.types',on_change='_on_change_dtype'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'point_id': fields.related(label='Shipping Point',obj='le.shipping.points',relatedy=['company_id'],domain=[('ptype','in',('o','b'))]),
	'place_id': fields.related(label='Loading Place',obj='le.loading.places',relatedy=['point_id'],domain=[('ptype','in',('o','b'))]),
	'category_id': fields.many2one(label='Category',obj='le.outbound.delivery.category'),
	'name': fields.varchar(label = 'Name'),
	'origin': fields.varchar(label = 'Origin'),
	'dod': fields.date(label='Date Of Delivery',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'items': fields.one2many(label='Items',obj='le.outbound.delivery.items',rel='delivery_id'),
	'roles': fields.one2many(label='Roles',obj='le.outbound.delivery.roles',rel='delivery_id'),
	#'picking': fields.one2many(label='Picking',obj='le.outbound.delivery.picking',rel='delivery_id'),
	#'loading': fields.one2many(label='Loading',obj='le.outbound.delivery.loading',rel='delivery_id'),
	#'shipping': fields.one2many(label='Shipping',obj='le.outbound.delivery.shipping',rel='delivery_id'),
	#'itrade': fields.one2many(label='International Trade',obj='le.outbound.delivery.itrade',rel='delivery_id',invisible="_itrade_invisible"),
	'texts': fields.one2many(label='Texts',obj='le.outbound.delivery.texts',rel='delivery_id'),
	'note': fields.text('Note')
	}

	def _itrade_ivisible(self,item,context={}):
		we_country = self._proxy.get('md.patner').select(['country_id'],[(self._proxy.get('md.partner')._getRecNameName(),'=',item['partner']['name'])],context)[0]['country_id']['name']
		return self._proxy.get('md.company').count([(self._proxy.get('md.company')._getRecNameName(),'=',item['company_id']['name']),('country_id','=',we_country)],context) > 0
	
	def _on_change_dtype(self,item,context={}):		
		roles = self._proxy.get('le.outbound.delivery.type.roles').select( ['role_id'],[('type_id','=',item['dtype']['name'])],context)
		for role in roles:
			item_role = self._proxy.get('le.outbound.delivery.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._proxy.get('le.outbound.delivery.types').select( ['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = self._proxy.get('le.delivery.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = self._proxy.get('le.outbound.delivery.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	_default = {
		'state':'draft'
	}

le_outbound_delivery()

class le_outbound_delivery_texts(Model):
	_name = 'le.outbound.delivery.texts'
	_description = 'Outbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'delivery_id': fields.many2one(label='Delivery',obj='le.outbound.delivery'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_outbound_delivery_texts()

class le_outbound_delivery_roles(Model):
	_name = 'le.outbound.delivery.roles'
	_description = 'Outbound Delivery Roles'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.outbound.delivery'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

le_inbound_delivery_roles()

class le_outbound_delivery_items(Model):
	_name = 'le.outbound.delivery.items'
	_description = 'Outbound Delivery Items'
	_columns = {
	'delivery_id': fields.many2one(obj = 'le.outbound.delivery',label = 'Delivery'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'packlist': fields.one2many(label='Pack List',obj='le.outbound.delivery.packlist',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='le.outbound.delivery.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _calculate_items(self,item,context={}):		
		if item['quantity'] and item['price'] and item['unit']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = self._proxy.get('md.vat.code').read(ids,['value','subtype_vat'],context)[0]
				v = r['value']
				s = r['subtype_vat']
				if s == 'e':
					item['vat_amount'] = item['amount'] * Decimal('0.%s' % (v,)) 
				elif s == 'i':
					item['vat_amount'] = item['amount'] - item['amount'] * Decimal('0.%s' % (v,)) 

		if 'amount' in item and item['amount']:
			item['total_amount'] = item['amount']
			if 'vat_amount' in item:
				if item['vat_amount']:
					item['total_amount'] += item['vat_amount'] 

		return None

	def _on_change_product(self,item,context={}):		
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

le_outbound_delivery_items()

class le_outbound_delivery_item_texts(Model):
	_name = 'le.outbound.delivery.item.texts'
	_description = 'Outbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='le.outbound.delivery.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_outbound_delivery_item_texts()

class le_outbound_delivery_packlist(Model):
	_name = 'le.outbound.delivery.packlist'
	_description = 'Packlist Of Outbound Delivery'
	_columns = {
	'item_id': fields.many2one(obj = 'le.outbound.delivery.items',label = 'Delivery Item'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'note': fields.text(label = 'Note')
	}

	def _calculate_items(self,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = self._proxy.get('md.vat.code').read(ids,['value','subtype_vat'],context)[0]
				v = r['value']
				s = r['subtype_vat']
				if s == 'e':
					item['vat_amount'] = item['amount'] * Decimal('0.%s' % (v,)) 
				elif s == 'i':
					item['vat_amount'] = item['amount'] - item['amount'] * Decimal('0.%s' % (v,)) 

		if 'amount' in item and item['amount']:
			item['total_amount'] = item['amount']
			if 'vat_amount' in item:
				if item['vat_amount']:
					item['total_amount'] += item['vat_amount'] 

		return None

	def _on_change_product(self,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self._proxy.get('md.purchase.product').select(['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit':1
	}

le_outbound_delivery_packlist()

# Internal
class le_internal_delivery(Model):
	_name = 'le.internal.delivery'
	_description = 'Internal Delivery'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',required = True,obj='le.internal.delivery.types',on_change='_on_change_dtype'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'point_id': fields.related(label='Shipping Point',obj='le.shipping.points',relatedy=['company_id'],domain=[('ptype','in',('i','b'))]),
	'place_id': fields.related(label='Loading Place',obj='le.loading.places',relatedy=['point_id'],domain=[('ptype','in',('i','b'))]),
	'category_id': fields.many2one(label='Category',obj='le.internal.delivery.category'),
	'name': fields.varchar(label = 'Name'),
	'origin': fields.varchar(label = 'Origin'),
	'dod': fields.date(label='Date Of Delivery',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('issuplier',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'items': fields.one2many(label='Items',obj='le.internal.delivery.items',rel='delivery_id'),
	'roles': fields.one2many(label='Roles',obj='le.internal.delivery.roles',rel='delivery_id'),
	'texts': fields.one2many(label='Texts',obj='le.internal.delivery.texts',rel='delivery_id'),
	'note': fields.text('Note')
	}

	def _on_change_dtype(self,item,context={}):		
		roles = self._proxy.get('le.internal.delivery.type.roles').select( ['role_id'],[('type_id','=',item['dtype']['name'])],context)
		for role in roles:
			item_role = self._proxy.get('le.internal.delivery.roles')._buildEmptyItem()
			item_role['role_id'] = role['role_id']
			item['roles'].append(item_role)
		
		types = self._proxy.get('le.internal.delivery.types').select( ['htschema'],[('name','=',item['dtype']['name'])],context)	
		texts1 = self._proxy.get('le.delivery.schema.texts').select( ['usage','code',{'texts':['seq','text_id']}],[('code','=',types[0]['htschema']['name'])],context)
		texts = texts1[0]['texts']
		seq = 0
		for text in texts:
			item_text = self._proxy.get('le.internal.delivery.texts')._buildEmptyItem()
			if text['seq']:
				item_text['seq'] = text['seq']
			else:
				item_text['seq'] = seq
				seq += 10
			item_text['text_id'] = text['text_id']
			item['texts'].append(item_text)

	_default = {
		'state':'draft'
	}

le_internal_delivery()

class le_internal_delivery_texts(Model):
	_name = 'le.internal.delivery.texts'
	_description = 'Internal Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'delivery_id': fields.many2one(label='Delivery',obj='le.internal.delivery'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_internal_delivery_texts()


class le_internal_delivery_roles(Model):
	_name = 'le.internal.delivery.roles'
	_description = 'Internal Delivery Roles'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.internal.delivery'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

le_internal_delivery_roles()

class le_internal_delivery_items(Model):
	_name = 'le.internal.delivery.items'
	_description = 'Internal Delivery Items'
	_columns = {
	'delivery_id': fields.many2one(obj = 'le.internal.delivery',label = 'Delivery'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'packlist': fields.one2many(label='Pack List',obj='le.inbound.delivery.packlist',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='le.internal.delivery.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _calculate_items(self,item,context={}):		
		if item['quantity'] and item['price'] and item['unit']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = self._proxy.get('md.vat.code').read(ids,['value','subtype_vat'],context)[0]
				v = r['value']
				s = r['subtype_vat']
				if s == 'e':
					item['vat_amount'] = item['amount'] * Decimal('0.%s' % (v,)) 
				elif s == 'i':
					item['vat_amount'] = item['amount'] - item['amount'] * Decimal('0.%s' % (v,)) 

		if 'amount' in item and item['amount']:
			item['total_amount'] = item['amount']
			if 'vat_amount' in item:
				if item['vat_amount']:
					item['total_amount'] += item['vat_amount'] 

		return None

	def _on_change_product(self,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self._proxy.get('md.purchase.product').select(['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

le_internal_delivery_items()

class le_internal_delivery_item_texts(Model):
	_name = 'le.internal.delivery.item.texts'
	_description = 'Inbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='le.internal.delivery.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.link(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_internal_delivery_item_texts()


class le_internal_delivery_packlist(Model):
	_name = 'le.internal.delivery.packlist'
	_description = 'Packlist Of Internal Delivery'
	_columns = {
	'item_id': fields.many2one(obj = 'le.internal.delivery.items',label = 'Delivery Item'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'note': fields.text(label = 'Note')
	}

	def _calculate_items(self,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = self._proxy.get('md.vat.code').read(ids,['value','subtype_vat'],context)[0]
				v = r['value']
				s = r['subtype_vat']
				if s == 'e':
					item['vat_amount'] = item['amount'] * Decimal('0.%s' % (v,)) 
				elif s == 'i':
					item['vat_amount'] = item['amount'] - item['amount'] * Decimal('0.%s' % (v,)) 

		if 'amount' in item and item['amount']:
			item['total_amount'] = item['amount']
			if 'vat_amount' in item:
				if item['vat_amount']:
					item['total_amount'] += item['vat_amount'] 

		return None

	def _on_change_product(self,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = self._proxy.get('md.purchase.product').select(['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit':1
	}

le_internal_delivery_packlist()

# inherit
class le_md_group_freight_cargo_product(Model):
	_name = 'le.md.group.freight.cargo.product'
	_description = 'Fleight Cargo Group Product'
	_columns = {
		'product_id': fields.many2one(label='Product',obj='md.product'),
		'group_freight_cargo_id': fields.many2one(label='Freight Cargo Group',obj='le.md.group.freight.cargo',required=True),
	}

le_md_group_freight_cargo_product()

class le_md_group_freight_cargo_product_inherit(ModelInherit):
	_name = 'le.md.group.freight.cargo.product.inherit'
	_description = 'Fleight Cargo Group Product Inherit'
	_inherit = {'md.product':{'_columns':['group_freight_cargo_product']}}
	_columns = {
		'group_freight_cargo_product': fields.one2many(label='Freight Cargo Group Product',obj='le.md.group.freight.cargo.product',rel='product_id'),
	}
	
le_md_group_freight_cargo_product_inherit()

