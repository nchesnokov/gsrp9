from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCmCostCollector(ViewModelSearchController):
	_name = "search:cm.cost.collector"
	_view_name = "cm.cost.collector/search"
	_description = "Cost Collector"

class ViewModelFindCmCostCollector(ViewModelFindController):
	_name = "find:cm.cost.collector"
	_view_name = "cm.cost.collector/find"
	_description = "Cost Collector"

class ViewModelListCmCostCollector(ViewModelListController):
	_name = "list:cm.cost.collector"
	_view_name = "cm.cost.collector/list"
	_description = "Cost Collector"

class ViewModelFormModalCmCostCollector(ViewModelFormModalController):
	_name = "form.modal:cm.cost.collector"
	_view_name = "cm.cost.collector/form.modal"
	_description = "Cost Collector"

class ViewModelFormCmCostCollector(ViewModelFormController):
	_name = "form:cm.cost.collector"
	_view_name = "cm.cost.collector/form"
	_description = "Cost Collector"
