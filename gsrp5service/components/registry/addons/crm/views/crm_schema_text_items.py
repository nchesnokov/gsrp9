from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmSchemaTextItems(ViewModelFind):
	_name = "model.find.crm.schema.text.items"
	_model = "crm.schema.text.items"
	_description = "Items Of Schema CRM Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']

class ViewModelO2MFormCrmSchemaTextItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.schema.text.items"
	_model = "crm.schema.text.items"
	_description = "Items Of Schema CRM Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']

class ViewModelO2MListCrmSchemaTextItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.schema.text.items"
	_model = "crm.schema.text.items"
	_description = "Items Of Schema CRM Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']
