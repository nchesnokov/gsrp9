from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

from decimal import Decimal

#customize

class le_shipping_points(Model):
	_name = 'le.shipping.points'
	_description = 'General Model Shipping Points'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'ptype': fields.selection(label='Usage',selections=[('i','Inbound'),('o','Outbound'),('b','Both')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'places': fields.one2many(label='Loading Place',obj='le.loading.places',rel='point_id'),
	'note': fields.text(label = 'Note')
	}

le_shipping_points()

class le_shipping_point_company_inherit(ModelInherit):
	_name = 'le.shipping.point.company.inherit'
	_description = 'Genaral Model Inherit For Shipping Point Company'
	_inherit = {'md.company':{'_columns':['points']}}
	_columns = {
		'points': fields.one2many(label='Shipping Points',obj='le.shipping.points',rel='company_id'),
	}
	
le_shipping_point_company_inherit()

class le_loading_places(Model):
	_name = 'le.loading.places'
	_description = 'General Model Loading Places'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'point_id': fields.many2one(label='Shiping Point',obj='le.shipping.points'	),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'note': fields.text(label = 'Note')
	}

le_loading_places()

class le_md_group_freight_cargo(Model):
	_name = 'le.md.group.freight.cargo'
	_description = 'General Model Fleight Cargo Group'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'descr': fields.varchar(label = 'Description',size=64,translate=True),
	'note': fields.text(label = 'Note')
	}
	

le_md_group_freight_cargo()

#Text
class le_delivery_texts(Model):
	_name = 'le.delivery.texts'
	_description = 'General Model Delivery Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

le_delivery_texts()

class le_delivery_schema_texts(Model):
	_name = 'le.delivery.schema.texts'
	_description = 'General Model Schema Of Delivery Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='le.delivery.schema.text.items',rel='schema_id')
	}
	
	_default = {
		'usage':'b'
	}

le_delivery_schema_texts()

class le_delivery_schema_text_items(Model):
	_name = 'le.delivery.schema.text.items'
	_description = 'General Model Items Of Schema Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='le.delivery.schema.texts'),
	'text_id': fields.many2one(label = 'Text',obj='le.delivery.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

le_delivery_schema_text_items()

# Text end

class le_inbound_delivery_types(Model):
	_name = 'le.inbound.delivery.types'
	_description = 'General Model Types Inbound Delivery'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='le.delivery.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='le.delivery.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='le.inbound.delivery.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

le_inbound_delivery_types()

class le_inbound_delivery_type_roles(Model):
	_name = 'le.inbound.delivery.type.roles'
	_description = 'General Model Role Inbound Delivery Types'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='le.inbound.delivery.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'note': fields.text(label = 'Note')
	}

le_inbound_delivery_type_roles()

class le_outbound_delivery_types(Model):
	_name = 'le.outbound.delivery.types'
	_description = 'General Model Types Outbound Delivery'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='le.delivery.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='le.delivery.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='le.outbound.delivery.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

le_outbound_delivery_types()

class le_outbound_delivery_type_roles(Model):
	_name = 'le.outbound.delivery.type.roles'
	_description = 'General Model Role Outbound Delivery Types'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='le.outbound.delivery.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'note': fields.text(label = 'Note')
	}

le_outbound_delivery_type_roles()

class le_internal_delivery_types(Model):
	_name = 'le.internal.delivery.types'
	_description = 'General Model Types Internal Delivery'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='le.delivery.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='le.delivery.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='le.internal.delivery.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

le_internal_delivery_types()

class le_internal_delivery_type_roles(Model):
	_name = 'le.internal.delivery.type.roles'
	_description = 'General Model Role Internal Delivery Types'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='le.internal.delivery.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','a'))]),
	'note': fields.text(label = 'Note')
	}

le_outbound_delivery_type_roles()

# end customize


class md_pack_product(Model):
	_name = 'md.pack.product'
	_description = 'General Model Pack Of Product'
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
	_inherit = {'md.product':{'_columns':['pack']},'md.recepture':{'_columns':['usage']}}
	_columns = {
		'pack': fields.one2many(label='Pack',obj='md.pack.product',rel='product_id'),
		'usage': fields.iSelection(selections=[('l','Pack')])
	}
	
md_pack_product_inherit()

class le_inbound_delivery_category(Model):
	_name = 'le.inbound.delivery.category'
	_description = 'General Model Category Inbound Delivery'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='le.inbound.delivery.category'),
	'childs_id': fields.one2many(obj = 'le.inbound.delivery.category',rel = 'parent_id',label = 'Childs'),
	'deliveries': fields.one2many(label='Deliveries',obj='le.inbound.delivery',rel='category_id',limit = 80),
	'note': fields.text(label = 'Note')
	}

le_inbound_delivery_category()

class le_outbound_delivery_category(Model):
	_name = 'le.outbound.delivery.category'
	_description = 'General Model Category Outbound Delivery'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='le.outbound.delivery.category'),
	'childs_id': fields.one2many(obj = 'le.outbound.delivery.category',rel = 'parent_id',label = 'Childs'),
	'deliveries': fields.one2many(label='Deliveries',obj='le.outbound.delivery',rel='category_id',limit = 80),
	'note': fields.text(label = 'Note')
	}

le_outbound_delivery_category()

class le_internal_delivery_category(Model):
	_name = 'le.internal.delivery.category'
	_description = 'General Model Category Internal Delivery'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='le.internal.delivery.category'),
	'childs_id': fields.one2many(obj = 'le.internal.delivery.category',rel = 'parent_id',label = 'Childs'),
	'deliveries': fields.one2many(label='Deliveries',obj='le.internal.delivery',rel='category_id',limit = 80),
	'note': fields.text(label = 'Note')
	}

le_internal_delivery_category()
# Inbound Delivery
class le_inbound_delivery(Model):
	_name = 'le.inbound.delivery'
	_description = 'General Model Inbound Delivery'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',required = True,obj='le.inbound.delivery.types',on_change='on_change_dtype'),
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
	'items': fields.one2many(label='Items',obj='le.inbound.delivery.items',rel='delivery_id'),
	'roles': fields.one2many(label='Roles',obj='le.inbound.delivery.roles',rel='delivery_id'),
	'texts': fields.one2many(label='Texts',obj='le.inbound.delivery.texts',rel='delivery_id'),
	'note': fields.text('Note')
	}

	def _on_change_dtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('le.inbound.delivery.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	_default = {
		'state':'draft'
	}

le_inbound_delivery()

class le_inbound_delivery_texts(Model):
	_name = 'le.inbound.delivery.texts'
	_description = 'General Model Inbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'delivery_id': fields.many2one(label='Delivery',obj='le.inbound.delivery'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_inbound_delivery_texts()

class le_inbound_delivery_roles(Model):
	_name = 'le.inbound.delivery.roles'
	_description = 'General Model Inbound Delivery Roles'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.inbound.delivery'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

le_inbound_delivery_roles()

class le_inbound_delivery_items(Model):
	_name = 'le.inbound.delivery.items'
	_description = 'General Model Inbound Delivery Items'
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
	'note': fields.text(label = 'Note')
	}

	def _calculate_items(self,cr,pool,uid,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = pool.get('md.vat.code').read(cr,pool,uid,ids,['value','subtype_vat'],context)[0]
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

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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

class le_inbound_delivery_item_texts(Model):
	_name = 'le.inbound.delivery.item.texts'
	_description = 'General Model Inbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='le.inbound.delivery.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_inbound_delivery_texts()



class le_inbound_delivery_packlist(Model):
	_name = 'le.inbound.delivery.packlist'
	_description = 'General Model Packlist Of Inbound Delivery'
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

	def _calculate_items(self,cr,pool,uid,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = pool.get('md.vat.code').read(cr,pool,uid,ids,['value','subtype_vat'],context)[0]
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

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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
	_description = 'General Model Outbound Delivery'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dod'
	_columns = {

	'dtype': fields.many2one(label='Type',required = True,obj='le.inbound.delivery.types',on_change='on_change_dtype'),
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

	def _itrade_ivisible(self,cr,pool,uid,item,context={}):
		we_country = pool.get('md.patner').select(cr,pool,uid,['country_id'],[(pool.get('md.partner')._getRecNameName(),'=',item['partner']['name'])],context)[0]['country_id']['name']
		return pool.get('md.company').count(cr,pool,uid,[(pool.get('md.company')._getRecNameName(),'=',item['company_id']['name']),('country_id','=',we_country)],context) > 0
	
	def _on_change_dtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('le.outbound.delivery.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	_default = {
		'state':'draft'
	}

le_outbound_delivery()

class le_outbound_delivery_texts(Model):
	_name = 'le.outbound.delivery.texts'
	_description = 'General Model Outbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'delivery_id': fields.many2one(label='Delivery',obj='le.outbound.delivery'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_outbound_delivery_texts()

class le_outbound_delivery_roles(Model):
	_name = 'le.outbound.delivery.roles'
	_description = 'General Model Outbound Delivery Roles'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.outbound.delivery'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

le_inbound_delivery_roles()

class le_outbound_delivery_items(Model):
	_name = 'le.outbound.delivery.items'
	_description = 'General Model Outbound Delivery Items'
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

	def _calculate_items(self,cr,pool,uid,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = pool.get('md.vat.code').read(cr,pool,uid,ids,['value','subtype_vat'],context)[0]
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

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.sale.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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
	_description = 'General Model Outbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='le.outbound.delivery.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_outbound_delivery_item_texts()

class le_outbound_delivery_packlist(Model):
	_name = 'le.outbound.delivery.packlist'
	_description = 'General Model Packlist Of Outbound Delivery'
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

	def _calculate_items(self,cr,pool,uid,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = pool.get('md.vat.code').read(cr,pool,uid,ids,['value','subtype_vat'],context)[0]
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

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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
	_description = 'General Model Internal Delivery'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',required = True,obj='le.internal.delivery.types',on_change='on_change_dtype'),
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

	def _on_change_dtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('le.internal.delivery.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	_default = {
		'state':'draft'
	}

le_internal_delivery()

class le_internal_delivery_texts(Model):
	_name = 'le.internal.delivery.texts'
	_description = 'General Model Inbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'delivery_id': fields.many2one(label='Delivery',obj='le.internal.delivery'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_internal_delivery_texts()


class le_internal_delivery_roles(Model):
	_name = 'le.internal.delivery.roles'
	_description = 'General Model Internal Delivery Roles'
	_columns = {
	'delivery_id': fields.many2one(label = 'Delivery',obj='le.internal.delivery'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

le_internal_delivery_roles()

class le_internal_delivery_items(Model):
	_name = 'le.internal.delivery.items'
	_description = 'General Model Internal Delivery Items'
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

	def _calculate_items(self,cr,pool,uid,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = pool.get('md.vat.code').read(cr,pool,uid,ids,['value','subtype_vat'],context)[0]
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

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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
	_description = 'General Model Inbound Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='le.internal.delivery.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='le.delivery.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

le_internal_delivery_item_texts()


class le_internal_delivery_packlist(Model):
	_name = 'le.internal.delivery.packlist'
	_description = 'General Model Packlist Of Internal Delivery'
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

	def _calculate_items(self,cr,pool,uid,item,context={}):		
		if item['quantity']:
			item['amount'] = item['quantity'] * item['price'] / item['unit'] 
		
		if 'amount' in item and item['amount'] and 'vat_code' in item and item['vat_code']:
			if type(item['vat_code']) == dict:
				ids = item['vat_code']['id']
			else:
				ids = item['vat_code']
			if ids:
				r = pool.get('md.vat.code').read(cr,pool,uid,ids,['value','subtype_vat'],context)[0]
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

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.purchase.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
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
	_description = 'General Model Fleight Cargo Group Product'
	_columns = {
		'product_id': fields.many2one(label='Product',obj='md.product'),
		'group_freight_cargo_id': fields.many2one(label='Freight Cargo Group',obj='le.md.group.freight.cargo',required=True),
	}

le_md_group_freight_cargo_product()

# class le_md_group_freight_cargo_product_inherit(ModelInherit):
	# _name = 'le.md.group.freight.cargo.product.inherit'
	# _description = 'General Model Fleight Cargo Group Product Inherit'
	# _inherit = {'md.product':{'_columns':['group_freight_cargo_product']}}
	# _columns = {
		# 'group_freight_cargo_product': fields.one2many(label='Freight Cargo Group Product',obj='le.md.group.freight.cargo.product',rel='product_id'),
	# }
	
# le_md_group_freight_cargo_product_inherit()

