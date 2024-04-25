from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcAuthObjs(ViewModelSearchController):
	_name = "search:bc.auth.objs"
	_view_name = "bc.auth.objs/search"
	_description = "Auth Objects"

class ViewModelFindBcAuthObjs(ViewModelFindController):
	_name = "find:bc.auth.objs"
	_view_name = "bc.auth.objs/find"
	_description = "Auth Objects"

class ViewModelListBcAuthObjs(ViewModelListController):
	_name = "list:bc.auth.objs"
	_view_name = "bc.auth.objs/list"
	_description = "Auth Objects"

class ViewModelFormModalBcAuthObjs(ViewModelFormModalController):
	_name = "form.modal:bc.auth.objs"
	_view_name = "bc.auth.objs/form.modal"
	_description = "Auth Objects"

class ViewModelFormBcAuthObjs(ViewModelFormController):
	_name = "form:bc.auth.objs"
	_view_name = "bc.auth.objs/form"
	_description = "Auth Objects"
