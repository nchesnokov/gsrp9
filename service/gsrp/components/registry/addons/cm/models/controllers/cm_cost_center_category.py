from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCmCostCenterCategory(ViewModelSearchController):
	_name = "search:cm.cost.center.category"
	_view_name = "cm.cost.center.category/search"
	_description = "Cost Center Category"

class ViewModelFindCmCostCenterCategory(ViewModelFindController):
	_name = "find:cm.cost.center.category"
	_view_name = "cm.cost.center.category/find"
	_description = "Cost Center Category"

class ViewModelListCmCostCenterCategory(ViewModelListController):
	_name = "list:cm.cost.center.category"
	_view_name = "cm.cost.center.category/list"
	_description = "Cost Center Category"

class ViewModelFormModalCmCostCenterCategory(ViewModelFormModalController):
	_name = "form.modal:cm.cost.center.category"
	_view_name = "cm.cost.center.category/form.modal"
	_description = "Cost Center Category"

class ViewModelFormCmCostCenterCategory(ViewModelFormController):
	_name = "form:cm.cost.center.category"
	_view_name = "cm.cost.center.category/form"
	_description = "Cost Center Category"

class ViewModelTreeCmCostCenterCategory(ViewModelTreeController):
	_name = "tree:cm.cost.center.category"
	_view_name = "cm.cost.center.category/tree"
	_description = "Cost Center Category"
