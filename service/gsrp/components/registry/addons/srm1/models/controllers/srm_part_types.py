from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmPartTypes(ViewModelSearchController):
	_name = "search:srm.part.types"
	_view_name = "srm.part.types/search"
	_description = "Types SRM Part"

class ViewModelFindSrmPartTypes(ViewModelFindController):
	_name = "find:srm.part.types"
	_view_name = "srm.part.types/find"
	_description = "Types SRM Part"

class ViewModelListSrmPartTypes(ViewModelListController):
	_name = "list:srm.part.types"
	_view_name = "srm.part.types/list"
	_description = "Types SRM Part"

class ViewModelFormModalSrmPartTypes(ViewModelFormModalController):
	_name = "form.modal:srm.part.types"
	_view_name = "srm.part.types/form.modal"
	_description = "Types SRM Part"

class ViewModelFormSrmPartTypes(ViewModelFormController):
	_name = "form:srm.part.types"
	_view_name = "srm.part.types/form"
	_description = "Types SRM Part"
