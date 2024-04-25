from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

from decimal import Decimal

#customize

class le_shipping_points(Model):
	_name = 'le.shipping.points'
	_description = 'Shipping Points'
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
	_description = 'Loading Places'
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
	_description = 'Fleight Cargo Group'
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
	_description = 'Delivery Texts'
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
	_description = 'Schema Of Delivery Texts'
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
	_description = 'Items Of Schema Delivery Texts'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='le.delivery.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='le.delivery.texts'),
	'descr': fields.link(ref='text_id.descr')
	}

le_delivery_schema_text_items()

# Text end

class le_inbound_delivery_types(Model):
	_name = 'le.inbound.delivery.types'
	_description = 'Types Inbound Delivery'
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
	_description = 'Role Inbound Delivery Types'
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
	_description = 'Types Outbound Delivery'
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
	_description = 'Role Outbound Delivery Types'
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
	_description = 'Types Internal Delivery'
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
	_description = 'Role Internal Delivery Types'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='le.internal.delivery.types', on_delete='c'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','a'))]),
	'note': fields.text(label = 'Note')
	}

le_outbound_delivery_type_roles()

class le_inbound_delivery_category(Model):
	_name = 'le.inbound.delivery.category'
	_description = 'Category Inbound Delivery'
	_class_model = 'C'
	_class_category = 'delivery'
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
	_description = 'Category Outbound Delivery'
	_class_model = 'C'
	_class_category = 'delivery'
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
	_description = 'Category Internal Delivery'
	_class_model = 'C'
	_class_category = 'delivery'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='le.internal.delivery.category'),
	'childs_id': fields.one2many(obj = 'le.internal.delivery.category',rel = 'parent_id',label = 'Childs'),
	'deliveries': fields.one2many(label='Deliveries',obj='le.internal.delivery',rel='category_id',limit = 80),
	'note': fields.text(label = 'Note')
	}

le_internal_delivery_category()

#Pricing
class le_pricing_group_levels(Model):
	_name = 'le.pricing.group.levels'
	_description = 'Sale Pricing Group Levels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

le_pricing_group_levels()

# end customize
