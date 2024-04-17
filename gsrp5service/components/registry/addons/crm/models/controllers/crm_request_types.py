from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmRequestTypes(ViewModelSearchController):
	_name = "search:crm.request.types"
	_view_name = "crm.request.types/search"
	_description = "Types CRM Request"

class ViewModelFindCrmRequestTypes(ViewModelFindController):
	_name = "find:crm.request.types"
	_view_name = "crm.request.types/find"
	_description = "Types CRM Request"

class ViewModelListCrmRequestTypes(ViewModelListController):
	_name = "list:crm.request.types"
	_view_name = "crm.request.types/list"
	_description = "Types CRM Request"

class ViewModelFormModalCrmRequestTypes(ViewModelFormModalController):
	_name = "form.modal:crm.request.types"
	_view_name = "crm.request.types/form.modal"
	_description = "Types CRM Request"

class ViewModelFormCrmRequestTypes(ViewModelFormController):
	_name = "form:crm.request.types"
	_view_name = "crm.request.types/form"
	_description = "Types CRM Request"
