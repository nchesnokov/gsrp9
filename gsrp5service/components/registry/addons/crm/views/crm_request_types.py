from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmRequestTypes(ViewModelSearch):
	_name = "model.search.crm.request.types"
	_model = "crm.request.types"
	_description = "Types CRM Request"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'required', 'note']

class ViewModelFindCrmRequestTypes(ViewModelFind):
	_name = "model.find.crm.request.types"
	_model = "crm.request.types"
	_description = "Types CRM Request"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'required', 'note']

class ViewModelListCrmRequestTypes(ViewModelList):
	_name = "model.list.crm.request.types"
	_model = "crm.request.types"
	_description = "Types CRM Request"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'roles', 'tis', 'required', 'note']

class ViewModelFormModalCrmRequestTypes(ViewModelFormModal):
	_name = "model.form.modal.crm.request.types"
	_model = "crm.request.types"
	_description = "Types CRM Request"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'roles', 'tis', 'required', 'note']

class ViewModelFormCrmRequestTypes(ViewModelForm):
	_name = "model.form.crm.request.types"
	_model = "crm.request.types"
	_description = "Types CRM Request"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'roles', 'tis', 'required', 'note']
