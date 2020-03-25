from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

#customize
#Text
class mrp_texts(Model):
	_name = 'mrp.texts'
	_description = 'General Model MRP Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

mrp_texts()

class mrp_schema_texts(Model):
	_name = 'mrp.schema.texts'
	_description = 'General Model Schema Of MRP Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='mrp.schema.text.items',rel='schema_id')
	}

mrp_schema_texts()

class mrp_schema_text_items(Model):
	_name = 'mrp.schema.text.items'
	_description = 'General Model Items Of Schema MRP Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='mrp.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

mrp_schema_text_items()

# Text end

class mrp_demand_types(Model):
	_name = 'mrp.demand.types'
	_description = 'General Model Types MRP Demand'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='mrp.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='mrp.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='mrp.demand.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

mrp_demand_types()

class mrp_demand_type_roles(Model):
	_name = 'mrp.demand.type.roles'
	_description = 'General Model Role MRP Demand Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='mrp.demand.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

mrp_demand_type_roles()

class mrp_request_types(Model):
	_name = 'mrp.request.types'
	_description = 'General Model Types MRP Request'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='mrp.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='mrp.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='mrp.request.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

mrp_request_types()

class mrp_request_type_roles(Model):
	_name = 'mrp.request.type.roles'
	_description = 'General Model Role MRP Request Types'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='mrp.request.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

mrp_request_type_roles()

# end customize


class md_mrp_product(Model):
	_name = 'md.mrp.product'
	_description = 'General Model Mrp Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'strategy': fields.selection(label='Strategy',selections=[('l','Lot'),('p','Point of order'),('n','Not planed')]),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'reserved_quantity': fields.numeric(label='Reserve Quantity',size=(11,3)),
	'min_quantity': fields.numeric(label='Min Quantity',size=(11,3)),
	'max_quantity': fields.numeric(label='Max Quantity',size=(11,3)),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_mrp_product()

class md_mrp_product_inherit(ModelInherit):
	_name = 'md.mrp.product.inherit'
	_description = 'Genaral Model Inherit For MRP Product'
	_inherit = {'md.product':{'_columns':['mrp']},'md.recepture':{'_columns':['usage']}}
	_columns = {
		'mrp': fields.one2many(label='MRP',obj='md.mrp.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('m',"Manufactured")])
	}
	
md_mrp_product_inherit()

class mrp_demand_category(Model):
	_name = 'mrp.demand.category'
	_description = 'General Model Category MRP Demand'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mrp.demand.category'),
	'childs_id': fields.one2many(obj = 'mrp.demand.category',rel = 'parent_id',label = 'Childs'),
	'demands': fields.one2many(label='Demands',obj='mrp.demand',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mrp_demand_category()

class mrp_request_category(Model):
	_name = 'mrp.request.category'
	_description = 'General Model Category MRP Request'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mrp.request.category'),
	'childs_id': fields.one2many(obj = 'mrp.request.category',rel = 'parent_id',label = 'Childs'),
	'requests': fields.one2many(label='Requests',obj='mrp.request',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mrp_request_category()

class mrp_demand(Model):
	_name = 'mrp.demand'
	_description = 'GeneralModel MRP Demand'
	_date = 'dod'
	_columns = {
	'dtype': fields.many2one(label='Type',obj='mrp.demand.types',on_change='on_change_dtype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='mrp.demand.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dod': fields.date(label='Date Of Demand',required=True),
	'from_date': fields.date(label='Begin Date Of Demand',required=True),
	'to_date': fields.date(label='End Date Of Demand',required=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='mrp.demand.items',rel='demand_id'),
	'roles': fields.one2many(label='Roles',obj='mrp.demand.roles',rel='demand_id'),
	'texts': fields.one2many(label='Texts',obj='mrp.demand.texts',rel='demand_id'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

	def _on_change_dtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('mrp.demand.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['dtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]



mrp_demand()

class mrp_demand_texts(Model):
	_name = 'mrp.demand.texts'
	_description = 'General Model MRP Demand Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'demand_id': fields.many2one(label='Demand',obj='mrp.demand'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mrp_demand_texts()


class mrp_demand_roles(Model):
	_name = 'mrp.demand.roles'
	_description = 'General Model MRP Demand Roles'
	_columns = {
	'demand_id': fields.many2one(label = 'Demand',obj='mrp.demand'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

mrp_demand_roles()


class mrp_demand_items(Model):
	_name = 'mrp.demand.items'
	_description = 'General Model MRP Demand Item'
	_rec_name = None
	_columns = {
	'demand_id': fields.many2one(obj = 'mrp.demand',label = 'Demand'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'schedules': fields.one2many(label='Schedule',obj='mrp.demand.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='mrp.demand.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='mrp.demand.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')}

mrp_demand_items()

class mrp_demand_item_texts(Model):
	_name = 'mrp.demand.item.texts'
	_description = 'General Model MRP Demand Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='mrp.demand.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mrp_demand_item_texts()


class mrp_demand_item_roles(Model):
	_name = 'mrp.demand.item.roles'
	_description = 'General Model MRP Demand Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='mrp.demand.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner',domain=[('ispeople',)])
	}

mrp_demand_item_roles()


class mrp_demand_delivery_schedules(Model):
	_name = 'mrp.demand.delivery.schedules'
	_description = 'General Model MRP Demand Delivery Schedule'
	_rec_name = None
	_columns = {
	'item_id': fields.many2one(obj = 'mrp.demand.items',label = 'Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

mrp_demand_delivery_schedules()

####
class mrp_request(Model):
	_name = 'mrp.request'
	_description = 'GeneralModel MRP Request'
	_date = 'dor'
	_columns = {
	'rtype': fields.many2one(label='Type',obj='mrp.request.types',on_change='on_change_rtype'),
	'name': fields.varchar(label = 'Name'),
	'company': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='mrp.request.category'),
	'origin': fields.varchar(label = 'Origin'),
	'dor': fields.date(label='Date Of Request',required=True),
	'from_date': fields.date(label='Begin Date Of Request',required=True),
	'to_date': fields.date(label='End Date Of Request',required=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'items': fields.one2many(label='Items',obj='mrp.request.items',rel='request_id'),
	'roles': fields.one2many(label='Roles',obj='mrp.request.roles',rel='request_id'),
	'texts': fields.one2many(label='Texts',obj='mrp.request.texts',rel='request_id'),
	'note': fields.text('Note')}

	def _on_change_rtype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('mrp.request.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['rtype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	_default = {
		'state':'draft'
	}

mrp_request()

class mrp_request_texts(Model):
	_name = 'mrp.request.texts'
	_description = 'General Model MRP Request Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'request_id': fields.many2one(label='Request',obj='mrp.request'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mrp_request_texts()


class mrp_request_roles(Model):
	_name = 'mrp.request.roles'
	_description = 'General Model Purchase Invoice Roles'
	_columns = {
	'invoice_id': fields.many2one(label = 'Request',obj='mrp.request'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

mrp_request_roles()


class mrp_request_items(Model):
	_name = 'mrp.request.items'
	_description = 'General Model MRP Request Item'
	_rec_name = None
	_columns = {
	'request_id': fields.many2one(obj = 'mrp.request',label = 'Request'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'schedules': fields.one2many(label='Schedule',obj='mrp.request.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='mrp.request.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='mrp.request.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')}

mrp_request_items()

class mrp_request_item_texts(Model):
	_name = 'mrp.request.item.texts'
	_description = 'General Model MRP Request Item Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='mrp.request.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='mrp.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

mrp_request_item_texts()


class mrp_request_item_roles(Model):
	_name = 'mrp.request.item.roles'
	_description = 'General Model MRP Request Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='mrp.request.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('S','B'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

mrp_request_item_roles()


class mrp_request_delivery_schedules(Model):
	_name = 'mrp.request.delivery.schedules'
	_description = 'General Model MRP Request Delivery Schedule'
	_rec_name = None
	_columns = {
	'item_id': fields.many2one(obj = 'mrp.request.items',label = 'Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

mrp_request_delivery_schedules()
