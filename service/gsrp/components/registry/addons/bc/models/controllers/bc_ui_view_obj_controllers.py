from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUiViewObjControllers(ViewModelSearchController):
	_name = "search:bc.ui.view.obj.controllers"
	_view_name = "bc.ui.view.obj.controllers/search"
	_description = "UI Controller Of View"

class ViewModelFindBcUiViewObjControllers(ViewModelFindController):
	_name = "find:bc.ui.view.obj.controllers"
	_view_name = "bc.ui.view.obj.controllers/find"
	_description = "UI Controller Of View"

class ViewModelListBcUiViewObjControllers(ViewModelListController):
	_name = "list:bc.ui.view.obj.controllers"
	_view_name = "bc.ui.view.obj.controllers/list"
	_description = "UI Controller Of View"

class ViewModelFormModalBcUiViewObjControllers(ViewModelFormModalController):
	_name = "form.modal:bc.ui.view.obj.controllers"
	_view_name = "bc.ui.view.obj.controllers/form.modal"
	_description = "UI Controller Of View"

class ViewModelFormBcUiViewObjControllers(ViewModelFormController):
	_name = "form:bc.ui.view.obj.controllers"
	_view_name = "bc.ui.view.obj.controllers/form"
	_description = "UI Controller Of View"
