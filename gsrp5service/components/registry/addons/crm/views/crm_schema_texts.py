from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmSchemaTexts(ViewModelSearch):
	_name = "model.search.crm.schema.texts"
	_model = "crm.schema.texts"
	_description = "Schema Of CRM Texts"
	_columns = ['usage', 'code', 'descr']

class ViewModelFindCrmSchemaTexts(ViewModelFind):
	_name = "model.find.crm.schema.texts"
	_model = "crm.schema.texts"
	_description = "Schema Of CRM Texts"
	_columns = ['usage', 'code', 'descr']

class ViewModelListCrmSchemaTexts(ViewModelList):
	_name = "model.list.crm.schema.texts"
	_model = "crm.schema.texts"
	_description = "Schema Of CRM Texts"
	_columns = ['usage', 'code', 'descr', 'texts']

class ViewModelFormModalCrmSchemaTexts(ViewModelFormModal):
	_name = "model.form.modal.crm.schema.texts"
	_model = "crm.schema.texts"
	_description = "Schema Of CRM Texts"
	_columns = ['usage', 'code', 'descr', 'texts']

class ViewModelFormCrmSchemaTexts(ViewModelForm):
	_name = "model.form.crm.schema.texts"
	_model = "crm.schema.texts"
	_description = "Schema Of CRM Texts"
	_columns = ['usage', 'code', 'descr', 'texts']
