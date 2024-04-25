from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcAccessObjs(ViewModelSearchController):
	_name = "search:bc.access.objs"
	_view_name = "bc.access.objs/search"
	_description = "Access Objects"

class ViewModelFindBcAccessObjs(ViewModelFindController):
	_name = "find:bc.access.objs"
	_view_name = "bc.access.objs/find"
	_description = "Access Objects"

class ViewModelListBcAccessObjs(ViewModelListController):
	_name = "list:bc.access.objs"
	_view_name = "bc.access.objs/list"
	_description = "Access Objects"

class ViewModelFormModalBcAccessObjs(ViewModelFormModalController):
	_name = "form.modal:bc.access.objs"
	_view_name = "bc.access.objs/form.modal"
	_description = "Access Objects"

class ViewModelFormBcAccessObjs(ViewModelFormController):
	_name = "form:bc.access.objs"
	_view_name = "bc.access.objs/form"
	_description = "Access Objects"
