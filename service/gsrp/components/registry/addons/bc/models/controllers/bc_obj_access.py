from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcObjAccess(ViewModelSearchController):
	_name = "search:bc.obj.access"
	_view_name = "bc.obj.access/search"
	_description = "Obj Access"

class ViewModelFindBcObjAccess(ViewModelFindController):
	_name = "find:bc.obj.access"
	_view_name = "bc.obj.access/find"
	_description = "Obj Access"

class ViewModelListBcObjAccess(ViewModelListController):
	_name = "list:bc.obj.access"
	_view_name = "bc.obj.access/list"
	_description = "Obj Access"

class ViewModelFormModalBcObjAccess(ViewModelFormModalController):
	_name = "form.modal:bc.obj.access"
	_view_name = "bc.obj.access/form.modal"
	_description = "Obj Access"

class ViewModelFormBcObjAccess(ViewModelFormController):
	_name = "form:bc.obj.access"
	_view_name = "bc.obj.access/form"
	_description = "Obj Access"
