from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmDemandCategory(ViewModelSearchController):
	_name = "search:srm.demand.category"
	_view_name = "srm.demand.category/search"
	_description = "Category SRM Demand"

class ViewModelFindSrmDemandCategory(ViewModelFindController):
	_name = "find:srm.demand.category"
	_view_name = "srm.demand.category/find"
	_description = "Category SRM Demand"

class ViewModelListSrmDemandCategory(ViewModelListController):
	_name = "list:srm.demand.category"
	_view_name = "srm.demand.category/list"
	_description = "Category SRM Demand"

class ViewModelFormModalSrmDemandCategory(ViewModelFormModalController):
	_name = "form.modal:srm.demand.category"
	_view_name = "srm.demand.category/form.modal"
	_description = "Category SRM Demand"

class ViewModelFormSrmDemandCategory(ViewModelFormController):
	_name = "form:srm.demand.category"
	_view_name = "srm.demand.category/form"
	_description = "Category SRM Demand"

class ViewModelTreeSrmDemandCategory(ViewModelTreeController):
	_name = "tree:srm.demand.category"
	_view_name = "srm.demand.category/tree"
	_description = "Category SRM Demand"
