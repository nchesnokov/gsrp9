
from orm import fields
from orm.model import Model

class ml_category(Model):
	_name = 'ml.category'
	_description = 'General Model Mashine Learning Category'
	_columns = {'name': fields.varchar(label = 'Name',size=64,translate=True)}

ml_category()
