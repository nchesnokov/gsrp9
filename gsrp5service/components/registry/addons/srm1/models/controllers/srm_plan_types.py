from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmPlanTypes(ViewModelSearchController):
	_name = "search:srm.plan.types"
	_view_name = "srm.plan.types/search"
	_description = "Types SRM Plan"

class ViewModelFindSrmPlanTypes(ViewModelFindController):
	_name = "find:srm.plan.types"
	_view_name = "srm.plan.types/find"
	_description = "Types SRM Plan"

class ViewModelListSrmPlanTypes(ViewModelListController):
	_name = "list:srm.plan.types"
	_view_name = "srm.plan.types/list"
	_description = "Types SRM Plan"

class ViewModelFormModalSrmPlanTypes(ViewModelFormModalController):
	_name = "form.modal:srm.plan.types"
	_view_name = "srm.plan.types/form.modal"
	_description = "Types SRM Plan"

class ViewModelFormSrmPlanTypes(ViewModelFormController):
	_name = "form:srm.plan.types"
	_view_name = "srm.plan.types/form"
	_description = "Types SRM Plan"
