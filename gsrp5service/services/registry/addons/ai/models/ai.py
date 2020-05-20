
from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

class ai_category(Model):
	_name = 'ai.category'
	_description = 'Artificial Intelligence Category'
	_columns = {'name': fields.varchar(label = 'Name',size=64,translate=True)}

ai_category()

class ai_model(Model):
	_name = 'ai.model'
	_description = 'Artificial Intelligence Model'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'method': fields.selection(label = 'Method',selections=[('svm','SVM'),('monte-karlo','Monte Carlo'),('regression','Regression')]),
	'meta': fields.json(label='Data')
	}

ai_model()
