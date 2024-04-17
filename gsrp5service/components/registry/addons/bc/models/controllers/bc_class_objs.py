from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcClassObjs(ViewModelSearchController):
	_name = "search:bc.class.objs"
	_view_name = "bc.class.objs/search"
	_description = "Class Objs"

class ViewModelFindBcClassObjs(ViewModelFindController):
	_name = "find:bc.class.objs"
	_view_name = "bc.class.objs/find"
	_description = "Class Objs"

class ViewModelListBcClassObjs(ViewModelListController):
	_name = "list:bc.class.objs"
	_view_name = "bc.class.objs/list"
	_description = "Class Objs"

class ViewModelFormModalBcClassObjs(ViewModelFormModalController):
	_name = "form.modal:bc.class.objs"
	_view_name = "bc.class.objs/form.modal"
	_description = "Class Objs"

class ViewModelFormBcClassObjs(ViewModelFormController):
	_name = "form:bc.class.objs"
	_view_name = "bc.class.objs/form"
	_description = "Class Objs"
