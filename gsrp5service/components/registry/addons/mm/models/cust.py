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
	'schema_id': fields.many2one(label = 'Schema',obj='mm.schema.texts',rel='texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.referenced(label = 'Text',obj='mm.texts'),
	#'descr': fields.referenced(ref='text_id.descr')
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
	'htschema': fields.referenced(label='Text Schema Of Head',obj='mm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.referenced(label='Text Schema Of Item',obj='mm.schema.texts',domain=[('usage','in',('i','b'))]),
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
	'type_id': fields.many2one(label = 'Type',obj='mm.production.order.types',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','p','a'))]),
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
	'htschema': fields.referenced(label='Text Schema Of Head',obj='mm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.referenced(label='Text Schema Of Item',obj='mm.schema.texts',domain=[('usage','in',('i','b'))]),
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
	'type_id': fields.many2one(label = 'Type',obj='mm.technologic.order.types',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','p','a'))]),
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
	'htschema': fields.referenced(label='Text Schema Of Head',obj='mm.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.referenced(label='Text Schema Of Item',obj='mm.schema.texts',domain=[('usage','in',('i','b'))]),
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
	'type_id': fields.many2one(label = 'Type',obj='mm.disassembly.order.types',rel='roles'),
	'role_id': fields.referenced(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','p','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_order_type_roles()

class mm_workcenter_category(Model):
	_name = 'mm.workcenter.category'
	_description = 'Category Workcenter'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.workcenter.category',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'mm.workcenter.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'workcenters': fields.one2many(label='Orders',obj='mm.workcenters',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_workcenter_category()

class mm_production_order_category(Model):
	_name = 'mm.production.order.category'
	_description = 'Category Production Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.production.order.category',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'mm.production.order.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'orders': fields.one2many(label='Orders',obj='mm.production.orders',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_production_order_category()

class mm_technologic_order_category(Model):
	_name = 'mm.technologic.order.category'
	_description = 'Category Technologic Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.technologic.order.category',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'mm.technologic.order.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'orders': fields.one2many(label='Orders',obj='mm.technologic.orders',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_technologic_order_category()

class mm_disassembly_order_category(Model):
	_name = 'mm.disassembly.order.category'
	_description = 'Category Disassembly Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.disassembly.order.category',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'mm.disassembly.order.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'orders': fields.one2many(label='Orders',obj='mm.disassembly.orders',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_order_category()
# workcenter
class mm_workcenters(Model):
	_name = 'mm.workcenters'
	_description = 'Workcenter'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='mm.workcenter.category',rel='workcenters'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'wctype': fields.selection(label='Type',selections=[('p','Production'),('t','Technology'),('d','Disassembly'),('a','All')]),
	'cost_peer_hour': fields.numeric(label='Cost Peer Hours',size=(11,2)),
	'cost_peer_cicle': fields.numeric(label='Cost Peer Cicles',size=(11,2)),
	'currency': fields.referenced(label='Currency',obj='md.currency',required=True),
	'products': fields.one2many(label='Products',obj='mm.workcenter.products',rel='workcenter_id',limit = 80),
	'note': fields.text(label = 'Note')
	}

mm_workcenters()

class mm_workcenter_products(Model):
	_name = 'mm.workcenter.products'
	_description = 'Workcenter Products'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'workcenter_id': fields.many2one(label='Workcenter',obj='mm.workcenters',rel='products'),
	'product': fields.referenced(label='Product',obj='md.product'),
	'prices': fields.one2many(label='Prices',obj='mm.workcenter.product.prices',rel='product_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_workcenter_products()

class mm_workcenter_product_prices(Model):
	_name = 'mm.workcenter.product.prices'
	_description = 'Workcenter Product Prices'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='mm.workcenter.products',rel='prices'),
	'from_date': fields.datetime(label='From',timezone=True),
	'to_date': fields.datetime(label='To',timezone=True),
	'price': fields.numeric(label='Price Peer Hours',size=(13,2)),
	'currency': fields.referenced(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.referenced(label="Unit Of Price Peer Hours",obj='md.uom',domain=[('quantity_id','=','Time')]),
	'note': fields.text(label = 'Note')
	}

mm_workcenter_product_prices()

# Operations
class mm_map_op_category(Model):
	_name = 'mm.map.op.category'
	_description = 'Category operation of map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.map.op.category',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'mm.map.op.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'ops': fields.one2many(label='Maps',obj='mm.map.ops',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_map_op_category()

class mm_map_ops(Model):
	_name = 'mm.map.ops'
	_description = 'Operation of map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='mm.map.op.category',rel='ops'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'company': fields.referenced(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols=['company','name'],translate = True,required = True),
	'usage': fields.selection(label='Usage',selections=[('p','Production'),('t','Technology'),('d','Disassembly'),('a','All')]),
	'note': fields.text(label = 'Note')
	}

mm_map_ops()

# Production map
class mm_production_map_category(Model):
	_name = 'mm.production.map.category'
	_description = 'Category Production Map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.production.map.category',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'mm.production.map.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'maps': fields.one2many(label='Maps',obj='mm.production.maps',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_production_map_category()

class mm_production_maps(Model):
	_name = 'mm.production.maps'
	_description = 'Production Map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='mm.production.map.category',rel='maps'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'company': fields.referenced(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols=['company','name'],translate = True,required = True),
	'bom': fields.referenced(label='BoM',obj='md.boms',on_change='_on_change_bom'),
	'ops': fields.one2many(obj = 'mm.production.map.ops',rel = 'op_id',label = 'Operations'),
	'note': fields.text(label = 'Note')
	}

mm_production_maps()

class mm_production_map_ops(Model):
	_name = 'mm.production.map.ops'
	_description = 'Operations of production map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'op_id': fields.many2one(label='Operation',obj='mm.production.maps',rel='ops'),
	'prev':  fields.referenced(label='Prev',obj='mm.map.ops',domain=[('usage','in',('p','a'))]),
	'op':  fields.referenced(label='Operation',obj='mm.map.ops',domain=[('usage','in',('p','a'))],required=True),
	'next': fields.referenced(label='Next',obj='mm.map.ops',domain=[('usage','in',('p','a'))]),
	'workcenter': fields.referenced(label='Workcenter',obj='mm.workcenters',required=True),
	'duration': fields.numeric(label='Duration',size=(11,3),required=True),
	'uod': fields.referenced(label='Unit of duration',obj='md.uom',domain=[('quantity_id','=','Time')],required=True),
	'per_cicle': fields.boolean(label='Per Cicle'),
	'note': fields.text(label = 'Note')
	}

mm_production_map_ops()

# technology map

class mm_technologic_map_category(Model):
	_name = 'mm.technologic.map.category'
	_description = 'Category Technologic Map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.technologic.map.category',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'mm.technologic.map.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'maps': fields.one2many(label='Maps',obj='mm.technologic.maps',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_technologic_map_category()

class mm_technologic_maps(Model):
	_name = 'mm.technologic.maps'
	_description = 'Technologic Map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='mm.technologic.map.category',rel='maps'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'company': fields.referenced(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols=['company','name'],translate = True,required = True),
	'bob': fields.referenced(label='BoB',obj='md.bobs',on_change='_on_change_bob'),
	'ops': fields.one2many(obj = 'mm.technologic.map.ops',rel = 'op_id',label = 'Operations'),
	'note': fields.text(label = 'Note')
	}

mm_technologic_maps()

class mm_technologic_map_ops(Model):
	_name = 'mm.technologic.map.ops'
	_description = 'Operations of technology map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'op_id': fields.many2one(label='Operation',obj='mm.technologic.maps',rel='ops'),
	'prev':  fields.referenced(label='Prev',obj='mm.map.ops',domain=[('usage','in',('t','a'))]),
	'op':  fields.referenced(label='Operation',obj='mm.map.ops',domain=[('usage','in',('t','a'))],required=True),
	'next': fields.referenced(label='Next',obj='mm.map.ops',domain=[('usage','in',('t','a'))]),
	'workcenter': fields.referenced(label='Workcenter',obj='mm.workcenters',required=True),
	'duration': fields.numeric(label='Duration',size=(11,3),required=True),
	'uod': fields.referenced(label='Unit of duration',obj='md.uom',domain=[('quantity_id','=','Time')],required=True),
	'per_cicle': fields.boolean(label='Per Cicle'),
	'note': fields.text(label = 'Note')
	}

mm_technologic_map_ops()

# Disassembly map

class mm_disassembly_map_category(Model):
	_name = 'mm.disassembly.map.category'
	_description = 'Category Disassembly Map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.disassembly.map.category',rel='childs_id'),
	'childs_id': fields.one2many(obj = 'mm.disassembly.map.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.tree(label='Full Name', translate = True,required = True),
	'maps': fields.one2many(label='Maps',obj='mm.disassembly.maps',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_map_category()

class mm_disassembly_maps(Model):
	_name = 'mm.disassembly.maps'
	_description = 'Disassembly map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='mm.disassembly.map.category',rel='maps'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'company': fields.referenced(label='Company',obj='md.company'),
	'fullname': fields.composite(label='Full Name', cols=['company','name'],translate = True,required = True),
	'mob': fields.referenced(label='MoB',obj='md.mobs',on_change='_on_change_mob'),
	'ops': fields.one2many(obj = 'mm.disassembly.map.ops',rel = 'op_id',label = 'Operations'),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_maps()

class mm_disassembly_map_ops(Model):
	_name = 'mm.disassembly.map.ops'
	_description = 'Operations of disassembly map'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'op_id': fields.many2one(label='Operation',obj='mm.disassembly.maps',rel='ops'),
	'prev':  fields.referenced(label='Prev',obj='mm.map.ops',domain=[('usage','in',('d','a'))]),
	'op':  fields.referenced(label='Operation',obj='mm.map.ops',domain=[('usage','in',('d','a'))],required=True),
	'next': fields.referenced(label='Next',obj='mm.map.ops',domain=[('usage','in',('d','a'))]),
	'workcenter': fields.referenced(label='Workcenter',obj='mm.workcenters',required=True),
	'duration': fields.numeric(label='Duration',size=(11,3),required=True),
	'uod': fields.referenced(label='Unit of duration',obj='md.uom',domain=[('quantity_id','=','Time')],required=True),
	'per_cicle': fields.boolean(label='Per Cicle'),
	'note': fields.text(label = 'Note')
	}

mm_disassembly_map_ops()
