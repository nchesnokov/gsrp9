from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCmCostOrder(ViewModelSearchController):
	_name = "search:cm.cost.order"
	_view_name = "cm.cost.order/search"
	_description = "Cost Order"

class ViewModelFindCmCostOrder(ViewModelFindController):
	_name = "find:cm.cost.order"
	_view_name = "cm.cost.order/find"
	_description = "Cost Order"

class ViewModelListCmCostOrder(ViewModelListController):
	_name = "list:cm.cost.order"
	_view_name = "cm.cost.order/list"
	_description = "Cost Order"

class ViewModelFormModalCmCostOrder(ViewModelFormModalController):
	_name = "form.modal:cm.cost.order"
	_view_name = "cm.cost.order/form.modal"
	_description = "Cost Order"

class ViewModelFormCmCostOrder(ViewModelFormController):
	_name = "form:cm.cost.order"
	_view_name = "cm.cost.order/form"
	_description = "Cost Order"
