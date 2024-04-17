from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmEvolutionTypes(ViewModelSearchController):
	_name = "search:srm.evolution.types"
	_view_name = "srm.evolution.types/search"
	_description = "Types SRM Evolution"

class ViewModelFindSrmEvolutionTypes(ViewModelFindController):
	_name = "find:srm.evolution.types"
	_view_name = "srm.evolution.types/find"
	_description = "Types SRM Evolution"

class ViewModelListSrmEvolutionTypes(ViewModelListController):
	_name = "list:srm.evolution.types"
	_view_name = "srm.evolution.types/list"
	_description = "Types SRM Evolution"

class ViewModelFormModalSrmEvolutionTypes(ViewModelFormModalController):
	_name = "form.modal:srm.evolution.types"
	_view_name = "srm.evolution.types/form.modal"
	_description = "Types SRM Evolution"

class ViewModelFormSrmEvolutionTypes(ViewModelFormController):
	_name = "form:srm.evolution.types"
	_view_name = "srm.evolution.types/form"
	_description = "Types SRM Evolution"
