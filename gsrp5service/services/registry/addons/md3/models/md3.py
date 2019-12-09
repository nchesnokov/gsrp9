
from orm import fields
from orm.model import Model,ModelInherit

class md_language(ModelInherit):
	_inherit = {"md.language":{'_columns':['runame']}}
	_name = 'md3.ru.language'
	_views = ['list','form','search']
	_description = 'General Model Language'
	_columns = {'runame': fields.varchar(label = 'Russian Name',size=64,translate=True)}

md_language()
