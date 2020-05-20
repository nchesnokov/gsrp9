
from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

class md_warehouse_product(Model):
	_name = 'md.warehouse.product'
	_description = 'Warehouse Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'strategy': fields.selection(label='Strategy',selections=[('l','LIfo'),('f','Fifo'),('n','Unordered'),('f','To fixed plase')]),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_warehouse_product()

class md_warehouse_product_inherit(ModelInherit):
	_name = 'md.warehouse.product.inherit'
	_description = 'Genaral Model Inherit For Warehouse Product'
	_inherit = {'md.product':{'_columns':['warehouse']}}
	_columns = {
		'warehouse': fields.one2many(label='Warehouse',obj='md.warehouse.product',rel='product_id')
	}
	
md_warehouse_product_inherit()

class wm_category(Model):
	_name = 'wm.category'
	_description = 'Warehouse Category'
	_columns = {'name': fields.varchar(label = 'Name',size=64,translate=True)}

wm_category()
