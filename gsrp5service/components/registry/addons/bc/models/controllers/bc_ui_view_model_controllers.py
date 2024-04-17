from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUiViewModelControllers(ViewModelSearchController):
	_name = "search:bc.ui.view.model.controllers"
	_view_name = "bc.ui.view.model.controllers/search"
	_description = "UI Model Controller Of View"

class ViewModelFindBcUiViewModelControllers(ViewModelFindController):
	_name = "find:bc.ui.view.model.controllers"
	_view_name = "bc.ui.view.model.controllers/find"
	_description = "UI Model Controller Of View"

class ViewModelListBcUiViewModelControllers(ViewModelListController):
	_name = "list:bc.ui.view.model.controllers"
	_view_name = "bc.ui.view.model.controllers/list"
	_description = "UI Model Controller Of View"

class ViewModelFormModalBcUiViewModelControllers(ViewModelFormModalController):
	_name = "form.modal:bc.ui.view.model.controllers"
	_view_name = "bc.ui.view.model.controllers/form.modal"
	_description = "UI Model Controller Of View"

class ViewModelFormBcUiViewModelControllers(ViewModelFormController):
	_name = "form:bc.ui.view.model.controllers"
	_view_name = "bc.ui.view.model.controllers/form"
	_description = "UI Model Controller Of View"
