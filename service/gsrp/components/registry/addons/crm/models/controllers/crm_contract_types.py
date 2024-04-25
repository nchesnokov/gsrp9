from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmContractTypes(ViewModelSearchController):
	_name = "search:crm.contract.types"
	_view_name = "crm.contract.types/search"
	_description = "Types Contract"

class ViewModelFindCrmContractTypes(ViewModelFindController):
	_name = "find:crm.contract.types"
	_view_name = "crm.contract.types/find"
	_description = "Types Contract"

class ViewModelListCrmContractTypes(ViewModelListController):
	_name = "list:crm.contract.types"
	_view_name = "crm.contract.types/list"
	_description = "Types Contract"

class ViewModelFormModalCrmContractTypes(ViewModelFormModalController):
	_name = "form.modal:crm.contract.types"
	_view_name = "crm.contract.types/form.modal"
	_description = "Types Contract"

class ViewModelFormCrmContractTypes(ViewModelFormController):
	_name = "form:crm.contract.types"
	_view_name = "crm.contract.types/form"
	_description = "Types Contract"
