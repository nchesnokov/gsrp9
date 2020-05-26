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
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','p','a'))]),
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
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','p','a'))]),
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
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('i','p','a'))]),
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
	'parent_id': fields.many2one(label='Parent',obj='mm.workcenter.category'),
	'childs_id': fields.one2many(obj = 'mm.workcenter.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'workcenters': fields.one2many(label='Orders',obj='mm.workcenters',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_workcenter_category()

class mm_route_category(Model):
	_name = 'mm.route.category'
	_description = 'Category Route'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.route.category'),
	'childs_id': fields.one2many(obj = 'mm.route.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
	'routes': fields.one2many(label='Orders',obj='mm.route',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

mm_route_category()

class mm_production_order_category(Model):
	_name = 'mm.production.order.category'
	_description = 'Category Production Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='mm.production.order.category'),
	'childs_id': fields.one2many(obj = 'mm.production.order.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
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
	'parent_id': fields.many2one(label='Parent',obj='mm.technologic.order.category'),
	'childs_id': fields.one2many(obj = 'mm.technologic.order.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
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
	'parent_id': fields.many2one(label='Parent',obj='mm.disassembly.order.category'),
	'childs_id': fields.one2many(obj = 'mm.disassembly.order.category',rel = 'parent_id',label = 'Childs'),
	'fullname': fields.composite(label='Full Name', translate = True,required = True, compute = '_compute_composite_tree'),
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
	'category_id': fields.many2one(label='Category',obj='mm.workcenter.category'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'wctype': fields.selection(label='Type',selections=[('p','Production'),('t','Technology'),('d','Disassembly'),('a','All')]),
	'cost_peer_hour': fields.numeric(label='Cost Peer Hours',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
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
	'workcenter_id': fields.many2one(label='Workcenter',obj='mm.workcenters'),
	'product': fields.many2one(label='Product',obj='md.product'),
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
	'product_id': fields.many2one(label='Product',obj='mm.workcenter.products'),
	'from_date': fields.datetime(label='From',timezone=True),
	'to_date': fields.datetime(label='To',timezone=True),
	'price': fields.numeric(label='Price Peer Hours',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price Peer Hours",obj='md.uom',),
	'note': fields.text(label = 'Note')
	}

mm_workcenter_product_prices()
#route
class mm_route(Model):
	_name = 'mm.route'
	_description = 'Route'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'category_id': fields.many2one(label='Category',obj='mm.route.category'),
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'rtype': fields.selection(label='Type',selections=[('p','Production'),('t','Technology'),('d','Disassembly'),('a','All')]),
	'items': fields.one2many(obj = 'mm.route.items',rel = 'route_id',label = 'Items'),
	'note': fields.text(label = 'Note')
	}

mm_route()

class mm_route_items(Model):
	_name = 'mm.route.items'
	_description = 'Route Items'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'route_id': fields.many2one(label='Route',obj='mm.route'),
	'workcenter': fields.many2one(label='Workcenter',obj='mm.workcenters'),
	'parent_id': fields.many2one(label='Parent',obj='mm.route.items'),
	'childs_id': fields.one2many(obj = 'mm.route.items',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

mm_route_items()

