from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcTypeObjs(ViewModelSearchController):
	_name = "search:bc.type.objs"
	_view_name = "bc.type.objs/search"
	_description = "Type Objects"

class ViewModelFindBcTypeObjs(ViewModelFindController):
	_name = "find:bc.type.objs"
	_view_name = "bc.type.objs/find"
	_description = "Type Objects"

class ViewModelListBcTypeObjs(ViewModelListController):
	_name = "list:bc.type.objs"
	_view_name = "bc.type.objs/list"
	_description = "Type Objects"

class ViewModelFormModalBcTypeObjs(ViewModelFormModalController):
	_name = "form.modal:bc.type.objs"
	_view_name = "bc.type.objs/form.modal"
	_description = "Type Objects"

class ViewModelFormBcTypeObjs(ViewModelFormController):
	_name = "form:bc.type.objs"
	_view_name = "bc.type.objs/form"
	_description = "Type Objects"
