from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

import web_pdb


#Pricing
class mm_pricing_group_levels(Model):
	_name = 'mm.pricing.group.levels'
	_description = 'Production Pricing Group Levels'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

mm_pricing_group_levels()

#Text
class mm_texts(Model):
	_name = 'mm.texts'
	_description = 'Manufactured Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

mm_texts()

class mm_schema_texts(Model):
	_name = 'mm.schema.texts'
	_description = 'Schema Of Manufactured Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='mm.schema.text.items',rel='schema_id')
	}

mm_schema_texts()

class mm_schema_text_items(Model):
	_name = 'mm.schema.text.items'
	_description = 'Items Of Schema Manufactured Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='mm.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='mm.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

mm_schema_text_items()

# Text end

class mm_production_order_types(Model):
	_name = 'mm.production.order.types'
	_description = 'Types Production Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'otype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='mm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='mm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='mm.production.order.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

mm_production_order_types()

class mm_production_order_type_roles(Model):
	_name = 'mm.production.order.type.roles'
	_description = 'Role Production Order Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='mm.production.order.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('mm','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

mm_production_order_type_roles()

class mm_technologic_order_types(Model):
	_name = 'mm.technologic.order.types'
	_description = 'Types Technologic Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'otype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='mm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='mm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='mm.technologic.order.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

mm_technologic_order_types()

class mm_technologic_order_type_roles(Model):
	_name = 'mm.technologic.order.type.roles'
	_description = 'Role Technologic Order Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='mm.technologic.order.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('mm','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

mm_technologic_order_type_roles()

#
class mm_disassembly_order_types(Model):
	_name = 'mm.disassembly.order.types'
	_description = 'Types Disassembly Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'otype': fields.selection(label='Type',selections=[('ord','Order'),('ap','Advance Payment'),('ps','Pseduo'),('dm','Debit Request'),('cr','Credit Request'),('rо','Return')]),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='mm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='mm.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='mm.disassembly.order.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_order_types()

class mm_disassembly_order_type_roles(Model):
	_name = 'mm.disassembly.order.type.roles'
	_description = 'Role Technologic Order Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='mm.disassembly.order.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('mm','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_order_type_roles()
