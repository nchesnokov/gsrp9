from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

class md_cost_product(Model):
	_name = 'md.cost.product'
	_description = 'General Model Cost Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_cost_product()

class md_cost_product_inherit(ModelInherit):
	_name = 'md.cost.product.inherit'
	_description = 'Genaral Model Inherit For Cost Product'
	_inherit = {'md.product':{'_columns':['cost']}}
	_columns = {
		'cost': fields.one2many(label='Cost',obj='md.cost.product',rel='product_id')
	}
	
md_cost_product_inherit()

class cm_cost_center_category(Model):
	_name = 'cm.cost.center.category'
	_description = 'General Model Cost Center Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='cm.cost.center.category'),
	'childs_id': fields.one2many(obj = 'cm.cost.center.category',rel = 'parent_id',label = 'Childs'),
	#'orders': fields.one2many(label='Orders',obj='purchase.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

cm_cost_center_category()

class cm_cost_order_category(Model):
	_name = 'cm.cost.order.category'
	_description = 'General Model Cost Order Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='cm.cost.order.category'),
	'childs_id': fields.one2many(obj = 'cm.cost.order.category',rel = 'parent_id',label = 'Childs'),
	#'orders': fields.one2many(label='Orders',obj='purchase.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

cm_cost_order_category()


class cm_cost_collector_category(Model):
	_name = 'cm.cost.collector.category'
	_description = 'General Model Cost Collector Category'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='cm.cost.collector.category'),
	'childs_id': fields.one2many(obj = 'cm.cost.collector.category',rel = 'parent_id',label = 'Childs'),
	#'orders': fields.one2many(label='Orders',obj='purchase.order',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

cm_cost_collector_category()


class cm_cost_center(Model):
	_name = 'cm.cost.center'
	_description = 'General Model Cost Center'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'category': fields.many2one(label="Category",obj="cm.cost.center.category"),
	'company': fields.many2one(label="Company",obj="md.company"),
	'currency': fields.many2one(label="Currency",obj="md.currency"),
	'dates': fields.one2many(label='Dates',obj='cm.cost.center.dates',rel='cost_center_id'),
	'note': fields.text(label = 'Note')
	}

cm_cost_center()

class cm_cost_center_dates(Model):
	_name = 'cm.cost.center.dates'
	_description = 'General Model Cost Center Dates'
	_date = 'cost_date'
	_columns = {
	'cost_center_id': fields.many2one(label="Cost Center",obj="cm.cost.center"),
	'cost_date': fields.date(label = 'Date'),
	'cost': fields.numeric(label='Cost',size=(15,2)),
	'note': fields.text(label = 'Note')
	}

cm_cost_center_dates()

class cm_cost_order(Model):
	_name = 'cm.cost.order'
	_description = 'General Model Cost Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'category': fields.many2one(label="Category",obj="cm.cost.order.category"),
	'company': fields.many2one(label="Company",obj="md.company"),
	'currency': fields.many2one(label="Currency",obj="md.currency"),
	'dates': fields.one2many(label='Dates',obj='cm.cost.order.dates',rel='cost_order_id'),
	'note': fields.text(label = 'Note')
	}

cm_cost_order()

class cm_cost_order_dates(Model):
	_name = 'cm.cost.order.dates'
	_description = 'General Model Cost Order Dates'
	_date = 'cost_date'
	_columns = {
	'cost_order_id': fields.many2one(label="Cost Order",obj="cm.cost.order"),
	'cost_date': fields.date(label = 'Date'),
	'cost': fields.numeric(label='Cost',size=(15,2)),
	'note': fields.text(label = 'Note')
	}

cm_cost_order_dates()

class cm_cost_collector(Model):
	_name = 'cm.cost.collector'
	_description = 'General Model Cost Collector'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'category': fields.many2one(label="Category",obj="cm.cost.collector.category"),
	'company': fields.many2one(label="Company",obj="md.company"),
	'currency': fields.many2one(label="Currency",obj="md.currency"),
	'dates': fields.one2many(label='Dates',obj='cm.cost.collector.dates',rel='cost_collector_id'),
	'note': fields.text(label = 'Note')
	}

cm_cost_collector()

class cm_cost_collector_dates(Model):
	_name = 'cm.cost.collector.dates'
	_description = 'General Model Cost Collector Dates'
	_date = 'cost_date'
	_columns = {
	'cost_collector_id': fields.many2one(label="Cost Collector",obj="cm.cost.collector"),
	'cost_date': fields.date(label = 'Date'),
	'cost': fields.numeric(label='Cost',size=(15,2)),
	'note': fields.text(label = 'Note')
	}

cm_cost_collector_dates()

class cm_corporations(Model):
	_name = 'cm.corporations'
	_description = 'General Model Corporations'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'usage': fields.selection(label='Usage',selections=[('o','One To One'),('m','One To Many')]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'companies': fields.one2many(label='Companies',obj='md.company',rel='corporation_id',readonly=True),
	'note': fields.text(label = 'Note')
	}
	
cm_corporations()

class cm_corporation_company_inherit(ModelInherit):
	_name = 'cm.corporation.company.inherit'
	_description = 'Genaral Model Inherit For Company'
	_inherit = {'md.company':{'_columns':['corporation_id']}}
	_columns = {
		'corporation_id': fields.many2one(label='Corparation',obj='cm.corporations'),
		
	}
	
cm_corporation_company_inherit()
