from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMrpDemandCategory(ViewModelSearchController):
	_name = "search:mrp.demand.category"
	_view_name = "mrp.demand.category/search"
	_description = "Category MRP Demand"

class ViewModelFindMrpDemandCategory(ViewModelFindController):
	_name = "find:mrp.demand.category"
	_view_name = "mrp.demand.category/find"
	_description = "Category MRP Demand"

class ViewModelListMrpDemandCategory(ViewModelListController):
	_name = "list:mrp.demand.category"
	_view_name = "mrp.demand.category/list"
	_description = "Category MRP Demand"

class ViewModelFormModalMrpDemandCategory(ViewModelFormModalController):
	_name = "form.modal:mrp.demand.category"
	_view_name = "mrp.demand.category/form.modal"
	_description = "Category MRP Demand"

class ViewModelFormMrpDemandCategory(ViewModelFormController):
	_name = "form:mrp.demand.category"
	_view_name = "mrp.demand.category/form"
	_description = "Category MRP Demand"

class ViewModelTreeMrpDemandCategory(ViewModelTreeController):
	_name = "tree:mrp.demand.category"
	_view_name = "mrp.demand.category/tree"
	_description = "Category MRP Demand"
