from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmEvolutionCategory(ViewModelSearchController):
	_name = "search:srm.evolution.category"
	_view_name = "srm.evolution.category/search"
	_description = "Category SRM Evolution"

class ViewModelFindSrmEvolutionCategory(ViewModelFindController):
	_name = "find:srm.evolution.category"
	_view_name = "srm.evolution.category/find"
	_description = "Category SRM Evolution"

class ViewModelListSrmEvolutionCategory(ViewModelListController):
	_name = "list:srm.evolution.category"
	_view_name = "srm.evolution.category/list"
	_description = "Category SRM Evolution"

class ViewModelFormModalSrmEvolutionCategory(ViewModelFormModalController):
	_name = "form.modal:srm.evolution.category"
	_view_name = "srm.evolution.category/form.modal"
	_description = "Category SRM Evolution"

class ViewModelFormSrmEvolutionCategory(ViewModelFormController):
	_name = "form:srm.evolution.category"
	_view_name = "srm.evolution.category/form"
	_description = "Category SRM Evolution"

class ViewModelTreeSrmEvolutionCategory(ViewModelTreeController):
	_name = "tree:srm.evolution.category"
	_view_name = "srm.evolution.category/tree"
	_description = "Category SRM Evolution"
