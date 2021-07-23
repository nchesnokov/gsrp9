from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

class wm_category(Model):
	_name = 'wm.category'
	_description = 'Warehouse Category'
	_class_model = 'C'
	_columns = {'name': fields.varchar(label = 'Name',size=64,translate=True)}

wm_category()
