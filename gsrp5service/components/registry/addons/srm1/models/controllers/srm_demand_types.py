from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmDemandTypes(ViewModelSearchController):
	_name = "search:srm.demand.types"
	_view_name = "srm.demand.types/search"
	_description = "Types SRM Demand"

class ViewModelFindSrmDemandTypes(ViewModelFindController):
	_name = "find:srm.demand.types"
	_view_name = "srm.demand.types/find"
	_description = "Types SRM Demand"

class ViewModelListSrmDemandTypes(ViewModelListController):
	_name = "list:srm.demand.types"
	_view_name = "srm.demand.types/list"
	_description = "Types SRM Demand"

class ViewModelFormModalSrmDemandTypes(ViewModelFormModalController):
	_name = "form.modal:srm.demand.types"
	_view_name = "srm.demand.types/form.modal"
	_description = "Types SRM Demand"

class ViewModelFormSrmDemandTypes(ViewModelFormController):
	_name = "form:srm.demand.types"
	_view_name = "srm.demand.types/form"
	_description = "Types SRM Demand"
