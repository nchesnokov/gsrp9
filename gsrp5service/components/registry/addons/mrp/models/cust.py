from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

#customize
#Text
class mrp_texts(Model):
	_name = 'mrp.texts'
	_description = 'MRP Texts'
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
	_description = 'Schema Of MRP Texts'
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
	_description = 'Items Of Schema MRP Texts'
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
	_description = 'Types MRP Demand'
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
	_description = 'Role MRP Demand Types'
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
	_description = 'Types MRP Request'
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
	_description = 'Role MRP Request Types'
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

