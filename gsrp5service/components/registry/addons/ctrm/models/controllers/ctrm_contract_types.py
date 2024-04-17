from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmContractTypes(ViewModelSearchController):
	_name = "search:ctrm.contract.types"
	_view_name = "ctrm.contract.types/search"
	_description = "Types CTRM Contract"

class ViewModelFindCtrmContractTypes(ViewModelFindController):
	_name = "find:ctrm.contract.types"
	_view_name = "ctrm.contract.types/find"
	_description = "Types CTRM Contract"

class ViewModelListCtrmContractTypes(ViewModelListController):
	_name = "list:ctrm.contract.types"
	_view_name = "ctrm.contract.types/list"
	_description = "Types CTRM Contract"

class ViewModelFormModalCtrmContractTypes(ViewModelFormModalController):
	_name = "form.modal:ctrm.contract.types"
	_view_name = "ctrm.contract.types/form.modal"
	_description = "Types CTRM Contract"

class ViewModelFormCtrmContractTypes(ViewModelFormController):
	_name = "form:ctrm.contract.types"
	_view_name = "ctrm.contract.types/form"
	_description = "Types CTRM Contract"
