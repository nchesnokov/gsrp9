from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchWmCategory(ViewModelSearchController):
	_name = "search:wm.category"
	_view_name = "wm.category/search"
	_description = "Warehouse Category"

class ViewModelFindWmCategory(ViewModelFindController):
	_name = "find:wm.category"
	_view_name = "wm.category/find"
	_description = "Warehouse Category"

class ViewModelListWmCategory(ViewModelListController):
	_name = "list:wm.category"
	_view_name = "wm.category/list"
	_description = "Warehouse Category"

class ViewModelFormModalWmCategory(ViewModelFormModalController):
	_name = "form.modal:wm.category"
	_view_name = "wm.category/form.modal"
	_description = "Warehouse Category"

class ViewModelFormWmCategory(ViewModelFormController):
	_name = "form:wm.category"
	_view_name = "wm.category/form"
	_description = "Warehouse Category"
