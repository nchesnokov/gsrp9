from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCmCostCollectorCategory(ViewModelSearchController):
	_name = "search:cm.cost.collector.category"
	_view_name = "cm.cost.collector.category/search"
	_description = "Cost Collector Category"

class ViewModelFindCmCostCollectorCategory(ViewModelFindController):
	_name = "find:cm.cost.collector.category"
	_view_name = "cm.cost.collector.category/find"
	_description = "Cost Collector Category"

class ViewModelListCmCostCollectorCategory(ViewModelListController):
	_name = "list:cm.cost.collector.category"
	_view_name = "cm.cost.collector.category/list"
	_description = "Cost Collector Category"

class ViewModelFormModalCmCostCollectorCategory(ViewModelFormModalController):
	_name = "form.modal:cm.cost.collector.category"
	_view_name = "cm.cost.collector.category/form.modal"
	_description = "Cost Collector Category"

class ViewModelFormCmCostCollectorCategory(ViewModelFormController):
	_name = "form:cm.cost.collector.category"
	_view_name = "cm.cost.collector.category/form"
	_description = "Cost Collector Category"

class ViewModelTreeCmCostCollectorCategory(ViewModelTreeController):
	_name = "tree:cm.cost.collector.category"
	_view_name = "cm.cost.collector.category/tree"
	_description = "Cost Collector Category"
