
from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

class md_quality_product(Model):
	_name = 'md.quality.product'
	_description = 'General Model Quality Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'type_quailty': fields.selection(label='Type',selections=[('i','Input'),('o','Output'),('m','Manufacturing')]),
	'note': fields.text(label = 'Note')
	}

md_quality_product()

class md_quality_product_inherit(ModelInherit):
	_name = 'md.quality.product.inherit'
	_description = 'Genaral Model Inherit For Quality Product'
	_inherit = {'md.product':{'_columns':['qm']}}
	_columns = {
		'qm': fields.one2many(label='Quality',obj='md.quality.product',rel='product_id')
	}
	
md_quality_product_inherit()

class qm_category(Model):
	_name = 'qm.category'
	_description = 'General Model Quantity Category'
	_columns = {'name': fields.varchar(label = 'Name',size=64,translate=True)}

qm_category()

