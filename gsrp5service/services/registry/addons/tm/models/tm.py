from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

class md_tm_product(Model):
	_name = 'md.tm.product'
	_description = 'TM Of Product'
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

md_tm_product()


class md_tm_product_inherit(ModelInherit):
	_name = 'md.tm.product.inherit'
	_description = 'Genaral Model Inherit For TM Product'
	_inherit = {'md.product':{'_columns':['tm']},'md.recepture':{'_columns':['usage']}}
	_columns = {
		'tm': fields.one2many(label='TM',obj='md.tm.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('t','Technical')])
	}
	
md_tm_product_inherit()

class tm_locations(Model):
	_name = 'tm.locations'
	_description = 'Locations'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('supplier', 'Vendor Location'),
        ('view', 'View'),
        ('internal', 'Internal Location'),
        ('customer', 'Customer Location'),
        ('inventory', 'Inventory Loss'),
        ('procurement', 'Procurement'),
        ('production', 'Production'),
        ('transit', 'Transit Location')]),
	'name': fields.varchar(label = 'Name'),
	'parent_id': fields.many2one(label = 'Parent',obj='tm.locations'),
	'childs_id': fields.one2many(label='Childs',obj='tm.locations',rel='parent_id'),
	'note': fields.text('Note')}

	_default = {
		'usage':'view'
	}


tm_locations()

class tm_maps(Model):
	_name = 'tm.maps'
	_description = 'Maps'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'otype': fields.selection(label='Type',selections=[('r','Repair'),('s','Service'),('d','Disassemkble')]),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'recepture_id': fields.many2one(label = 'Recepture',obj='md.recepture'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft',
		'otype':'s'
	}

tm_maps()

class tm_handlings(Model):
	_name = 'tm.handlings'
	_description = 'Handlings'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'map_id': fields.many2one(label = 'Map',obj='tm.maps'),
	'note': fields.text('Note')}

	_default = {
		'state':'draft'
	}

tm_handlings()

class tm_category_node(Model):
	_name = 'tm.category.node'
	_description = 'Category Node'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='tm.category.node'),
	'childs_id': fields.one2many(obj = 'tm.category.node',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

tm_category_node()

class tm_nodes(Model):
	_name = 'tm.nodes'
	_description = 'Nodes'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'category_id': fields.many2one(label='Category',obj='tm.category.node'),
	'parent_id': fields.many2one(label='Parent',obj='tm.nodes'),
	'childs_id': fields.one2many(obj = 'tm.nodes',rel = 'parent_id',label = 'Childs'),
	'items': fields.one2many(label='Items',obj='tm.node.items',rel='node_id'),
	'inactive': fields.boolean(label='Inactive'),
	'note': fields.text(label = 'Note')
	}

tm_nodes()

class tm_node_items(Model):
	_name = 'tm.node.items'
	_description = 'Node Items'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'node_id': fields.many2one(label='Node',obj='tm.nodes'),
	'parent_id': fields.many2one(label='Parent',obj='tm.node.items'),
	'childs_id': fields.one2many(obj = 'tm.node.items',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

tm_node_items()

class tm_category_equipment(Model):
	_name = 'tm.category.equipment'
	_description = 'Category Equipment'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='tm.category.equipment'),
	'childs_id': fields.one2many(obj = 'tm.category.equipment',rel = 'parent_id',label = 'Childs'),
	'note': fields.text(label = 'Note')
	}

tm_category_equipment()

class tm_template_equipment(Model):
	_name = 'tm.template.equipment'
	_description = 'Template Equipment'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'nodes': fields.one2many(obj = 'tm.template.nodes',rel = 'template_equipment_id',label = 'Nodes'),
	'maps': fields.one2many(obj = 'tm.template.maps',rel = 'template_equipment_id',label = 'Maps'),
	'handlings': fields.one2many(obj = 'tm.template.handlings',rel = 'template_equipment_id',label = 'Handlings'),
	'inactive': fields.boolean(label='InActive'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'state':'draft'
	}


tm_template_equipment()

class tm_template_nodes(Model):
	_name = 'tm.template.nodes'
	_description = 'Template Nodes'
	_columns = {
	'template_equipment_id': fields.many2one(label='Template',obj='tm.template.equipment'),
	'node_id': fields.many2one(label='Node',obj='tm.nodes'),
	'note': fields.text(label = 'Note')
	}

tm_template_nodes()

class tm_template_maps(Model):
	_name = 'tm.template.maps'
	_description = 'Template Maps'
	_columns = {
	'template_equipment_id': fields.many2one(label='Template',obj='tm.template.equipment'),
	'map_id': fields.many2one(label='Map',obj='tm.maps'),
	'note': fields.text(label = 'Note')
	}

tm_template_maps()

class tm_template_handlings(Model):
	_name = 'tm.template.handlings'
	_description = 'Template Handlings'
	_columns = {
	'template_equipment_id': fields.many2one(label='Template',obj='tm.template.equipment'),
	'handling_id': fields.many2one(label='Handling',obj='tm.handlings'),
	'otype': fields.selection(label='Type',selections=[('p','Primary'),('P','Periodical'),('l','Latest')]),
	'period': fields.integer(label='Period',required = True),
	'unit': fields.many2one(label="UoM",required=True,obj='md.uom',domain=[('quantity_id','=','Time')]),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'otype':'P'
	}


tm_template_handlings()

class tm_unit_equipments(Model):
	_name = 'tm.unit.equipments'
	_description = 'Unit Equipments'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'location_id': fields.many2one(label='Location',obj='tm.locations'),
	'template_id': fields.many2one(label='Template',obj='tm.template.equipment'),
	'category_id': fields.many2one(label='Category',obj='tm.category.equipment'),
	'serial_no': fields.varchar(label = 'Serial No',size=64,translate=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'inactive': fields.boolean(label='Inactive'),
	'orders': fields.one2many(obj = 'tm.unit.equipment.orders',rel = 'unit_equipment_id',label = 'Orders'),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
		'state':'draft'
	}

tm_unit_equipments()


class tm_orders(Model):
	_name = 'tm.orders'
	_description = 'Order'
	_date = 'doo'
	_columns = {
	'name': fields.varchar(label = 'Name'),
	'origin': fields.varchar(label = 'Origin'),
	'otype': fields.selection(label='Type',selections=[('r','Repair'),('d','Disassemble'),('s','Services')]),	
	'unit_equipment_id': fields.many2one(label='Unit Equipment',obj='tm.unit.equipments',required=True),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.datetime(label="Start date",timezone=True),
	'to_date': fields.datetime(label="End date",timezone=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','t'),'|',('usage','=','a')]),
	'items': fields.one2many(label='Items',obj='tm.order.items',rel='order_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'otype':'s'
	}

tm_orders()

class tm_order_items(Model):
	_name = 'tm.order.items'
	_description = 'Order Items'
	_columns = {
	'order_id': fields.many2one(obj = 'tm.orders',label = 'Order'),
	'product': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
		}

tm_order_items()

class tm_unit_equipment_orders(Model):
	_name = 'tm.unit.equipment.orders'
	_description = 'Unit Equipment Orders'
	_columns = {
	'unit_equipment_id': fields.many2one(label='Unit Equipment',obj='tm.unit.equipments'),
	'order_id': fields.many2one(label='Order',obj='tm.orders'),
	'state': fields.referenced(label='State',ref='order_id.state'),
	'start_date': fields.referenced(label='Start Date',ref='order_id.from_date'),
	'end_date': fields.referenced(label='End Date',ref='order_id.to_date'),
	'otype': fields.referenced(label='Type',ref='order_id.otype'),
	'note': fields.text(label='Note')
	}

tm_unit_equipment_orders()
