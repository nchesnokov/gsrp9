from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmContractTypes(ViewModelSearchController):
	_name = "search:srm.contract.types"
	_view_name = "srm.contract.types/search"
	_description = "Types SRM Contract"

class ViewModelFindSrmContractTypes(ViewModelFindController):
	_name = "find:srm.contract.types"
	_view_name = "srm.contract.types/find"
	_description = "Types SRM Contract"

class ViewModelListSrmContractTypes(ViewModelListController):
	_name = "list:srm.contract.types"
	_view_name = "srm.contract.types/list"
	_description = "Types SRM Contract"

class ViewModelFormModalSrmContractTypes(ViewModelFormModalController):
	_name = "form.modal:srm.contract.types"
	_view_name = "srm.contract.types/form.modal"
	_description = "Types SRM Contract"

class ViewModelFormSrmContractTypes(ViewModelFormController):
	_name = "form:srm.contract.types"
	_view_name = "srm.contract.types/form"
	_description = "Types SRM Contract"
