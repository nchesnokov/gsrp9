from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcModels(ViewModelSearchController):
	_name = "search:bc.models"
	_view_name = "bc.models/search"
	_description = "Models"

class ViewModelFindBcModels(ViewModelFindController):
	_name = "find:bc.models"
	_view_name = "bc.models/find"
	_description = "Models"

class ViewModelListBcModels(ViewModelListController):
	_name = "list:bc.models"
	_view_name = "bc.models/list"
	_description = "Models"

class ViewModelFormModalBcModels(ViewModelFormModalController):
	_name = "form.modal:bc.models"
	_view_name = "bc.models/form.modal"
	_description = "Models"

class ViewModelFormBcModels(ViewModelFormController):
	_name = "form:bc.models"
	_view_name = "bc.models/form"
	_description = "Models"
