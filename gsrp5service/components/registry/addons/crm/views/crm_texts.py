from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmTexts(ViewModelSearch):
	_name = "model.search.crm.texts"
	_model = "crm.texts"
	_description = "CRM Texts"
	_columns = ['code', 'descr']

class ViewModelFindCrmTexts(ViewModelFind):
	_name = "model.find.crm.texts"
	_model = "crm.texts"
	_description = "CRM Texts"
	_columns = ['code', 'descr']

class ViewModelListCrmTexts(ViewModelList):
	_name = "model.list.crm.texts"
	_model = "crm.texts"
	_description = "CRM Texts"
	_columns = ['code', 'descr']

class ViewModelFormModalCrmTexts(ViewModelFormModal):
	_name = "model.form.modal.crm.texts"
	_model = "crm.texts"
	_description = "CRM Texts"
	_columns = ['code', 'descr']

class ViewModelFormCrmTexts(ViewModelForm):
	_name = "model.form.crm.texts"
	_model = "crm.texts"
	_description = "CRM Texts"
	_columns = ['code', 'descr']
