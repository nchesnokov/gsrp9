from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmContractCategory(ViewModelSearchController):
	_name = "search:srm.contract.category"
	_view_name = "srm.contract.category/search"
	_description = "Category SRM Contract"

class ViewModelFindSrmContractCategory(ViewModelFindController):
	_name = "find:srm.contract.category"
	_view_name = "srm.contract.category/find"
	_description = "Category SRM Contract"

class ViewModelListSrmContractCategory(ViewModelListController):
	_name = "list:srm.contract.category"
	_view_name = "srm.contract.category/list"
	_description = "Category SRM Contract"

class ViewModelFormModalSrmContractCategory(ViewModelFormModalController):
	_name = "form.modal:srm.contract.category"
	_view_name = "srm.contract.category/form.modal"
	_description = "Category SRM Contract"

class ViewModelFormSrmContractCategory(ViewModelFormController):
	_name = "form:srm.contract.category"
	_view_name = "srm.contract.category/form"
	_description = "Category SRM Contract"

class ViewModelTreeSrmContractCategory(ViewModelTreeController):
	_name = "tree:srm.contract.category"
	_view_name = "srm.contract.category/tree"
	_description = "Category SRM Contract"
