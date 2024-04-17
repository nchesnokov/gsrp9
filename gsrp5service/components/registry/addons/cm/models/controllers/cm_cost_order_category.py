from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCmCostOrderCategory(ViewModelSearchController):
	_name = "search:cm.cost.order.category"
	_view_name = "cm.cost.order.category/search"
	_description = "Cost Order Category"

class ViewModelFindCmCostOrderCategory(ViewModelFindController):
	_name = "find:cm.cost.order.category"
	_view_name = "cm.cost.order.category/find"
	_description = "Cost Order Category"

class ViewModelListCmCostOrderCategory(ViewModelListController):
	_name = "list:cm.cost.order.category"
	_view_name = "cm.cost.order.category/list"
	_description = "Cost Order Category"

class ViewModelFormModalCmCostOrderCategory(ViewModelFormModalController):
	_name = "form.modal:cm.cost.order.category"
	_view_name = "cm.cost.order.category/form.modal"
	_description = "Cost Order Category"

class ViewModelFormCmCostOrderCategory(ViewModelFormController):
	_name = "form:cm.cost.order.category"
	_view_name = "cm.cost.order.category/form"
	_description = "Cost Order Category"

class ViewModelTreeCmCostOrderCategory(ViewModelTreeController):
	_name = "tree:cm.cost.order.category"
	_view_name = "cm.cost.order.category/tree"
	_description = "Cost Order Category"
