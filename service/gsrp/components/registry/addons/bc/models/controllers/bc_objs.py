from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcObjs(ViewModelSearchController):
	_name = "search:bc.objs"
	_view_name = "bc.objs/search"
	_description = "Objects"

class ViewModelFindBcObjs(ViewModelFindController):
	_name = "find:bc.objs"
	_view_name = "bc.objs/find"
	_description = "Objects"

class ViewModelListBcObjs(ViewModelListController):
	_name = "list:bc.objs"
	_view_name = "bc.objs/list"
	_description = "Objects"

class ViewModelFormModalBcObjs(ViewModelFormModalController):
	_name = "form.modal:bc.objs"
	_view_name = "bc.objs/form.modal"
	_description = "Objects"

class ViewModelFormBcObjs(ViewModelFormController):
	_name = "form:bc.objs"
	_view_name = "bc.objs/form"
	_description = "Objects"
