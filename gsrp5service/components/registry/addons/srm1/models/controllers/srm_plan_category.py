from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmPlanCategory(ViewModelSearchController):
	_name = "search:srm.plan.category"
	_view_name = "srm.plan.category/search"
	_description = "Category SRM Plan"

class ViewModelFindSrmPlanCategory(ViewModelFindController):
	_name = "find:srm.plan.category"
	_view_name = "srm.plan.category/find"
	_description = "Category SRM Plan"

class ViewModelListSrmPlanCategory(ViewModelListController):
	_name = "list:srm.plan.category"
	_view_name = "srm.plan.category/list"
	_description = "Category SRM Plan"

class ViewModelFormModalSrmPlanCategory(ViewModelFormModalController):
	_name = "form.modal:srm.plan.category"
	_view_name = "srm.plan.category/form.modal"
	_description = "Category SRM Plan"

class ViewModelFormSrmPlanCategory(ViewModelFormController):
	_name = "form:srm.plan.category"
	_view_name = "srm.plan.category/form"
	_description = "Category SRM Plan"

class ViewModelTreeSrmPlanCategory(ViewModelTreeController):
	_name = "tree:srm.plan.category"
	_view_name = "srm.plan.category/tree"
	_description = "Category SRM Plan"
