from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

class ewm_warehouse(Model):
	_name = 'ewm.warehouse'
	_description = 'Warehouse'
	_class_model = 'C'
	_class_category = 'warehouse'

	_columns = {
	'stock': fields.many2one(label='Stock',obj='st.stock',required = True),
	'name': fields.varchar(label = 'Name',required = True),
	'fullname': fields.composite(label = 'Fullname',cols=['stock','name'], translate = True,required = True, compute = '_compute_composite'),
	'products': fields.one2many(label='Products',readonly=True,obj='md.stock.product',rel='stock_id',limit=80),
	'note': fields.text(label = 'Note')}

ewm_warehouse()
