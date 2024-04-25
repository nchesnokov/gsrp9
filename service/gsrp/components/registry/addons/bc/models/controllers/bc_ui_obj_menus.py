from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchBcUiObjMenus(ViewModelSearchController):
	_name = "search:bc.ui.obj.menus"
	_view_name = "bc.ui.obj.menus/search"
	_description = "Object UI Menus"

class ViewModelFindBcUiObjMenus(ViewModelFindController):
	_name = "find:bc.ui.obj.menus"
	_view_name = "bc.ui.obj.menus/find"
	_description = "Object UI Menus"

class ViewModelListBcUiObjMenus(ViewModelListController):
	_name = "list:bc.ui.obj.menus"
	_view_name = "bc.ui.obj.menus/list"
	_description = "Object UI Menus"

class ViewModelFormModalBcUiObjMenus(ViewModelFormModalController):
	_name = "form.modal:bc.ui.obj.menus"
	_view_name = "bc.ui.obj.menus/form.modal"
	_description = "Object UI Menus"

class ViewModelFormBcUiObjMenus(ViewModelFormController):
	_name = "form:bc.ui.obj.menus"
	_view_name = "bc.ui.obj.menus/form"
	_description = "Object UI Menus"

class ViewModelTreeBcUiObjMenus(ViewModelTreeController):
	_name = "tree:bc.ui.obj.menus"
	_view_name = "bc.ui.obj.menus/tree"
	_description = "Object UI Menus"
