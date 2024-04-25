from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMrpDemandTypes(ViewModelSearchController):
	_name = "search:mrp.demand.types"
	_view_name = "mrp.demand.types/search"
	_description = "Types MRP Demand"

class ViewModelFindMrpDemandTypes(ViewModelFindController):
	_name = "find:mrp.demand.types"
	_view_name = "mrp.demand.types/find"
	_description = "Types MRP Demand"

class ViewModelListMrpDemandTypes(ViewModelListController):
	_name = "list:mrp.demand.types"
	_view_name = "mrp.demand.types/list"
	_description = "Types MRP Demand"

class ViewModelFormModalMrpDemandTypes(ViewModelFormModalController):
	_name = "form.modal:mrp.demand.types"
	_view_name = "mrp.demand.types/form.modal"
	_description = "Types MRP Demand"

class ViewModelFormMrpDemandTypes(ViewModelFormController):
	_name = "form:mrp.demand.types"
	_view_name = "mrp.demand.types/form"
	_description = "Types MRP Demand"
