from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmOrderTypes(ViewModelSearchController):
	_name = "search:crm.order.types"
	_view_name = "crm.order.types/search"
	_description = "Types CRM Order"

class ViewModelFindCrmOrderTypes(ViewModelFindController):
	_name = "find:crm.order.types"
	_view_name = "crm.order.types/find"
	_description = "Types CRM Order"

class ViewModelListCrmOrderTypes(ViewModelListController):
	_name = "list:crm.order.types"
	_view_name = "crm.order.types/list"
	_description = "Types CRM Order"

class ViewModelFormModalCrmOrderTypes(ViewModelFormModalController):
	_name = "form.modal:crm.order.types"
	_view_name = "crm.order.types/form.modal"
	_description = "Types CRM Order"

class ViewModelFormCrmOrderTypes(ViewModelFormController):
	_name = "form:crm.order.types"
	_view_name = "crm.order.types/form"
	_description = "Types CRM Order"
