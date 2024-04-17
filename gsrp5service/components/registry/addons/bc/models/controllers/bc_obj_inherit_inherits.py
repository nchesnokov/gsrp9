from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcObjInheritInherits(ViewModelSearchController):
	_name = "search:bc.obj.inherit.inherits"
	_view_name = "bc.obj.inherit.inherits/search"
	_description = "Inherit Columns To Objects"

class ViewModelFindBcObjInheritInherits(ViewModelFindController):
	_name = "find:bc.obj.inherit.inherits"
	_view_name = "bc.obj.inherit.inherits/find"
	_description = "Inherit Columns To Objects"

class ViewModelListBcObjInheritInherits(ViewModelListController):
	_name = "list:bc.obj.inherit.inherits"
	_view_name = "bc.obj.inherit.inherits/list"
	_description = "Inherit Columns To Objects"

class ViewModelFormModalBcObjInheritInherits(ViewModelFormModalController):
	_name = "form.modal:bc.obj.inherit.inherits"
	_view_name = "bc.obj.inherit.inherits/form.modal"
	_description = "Inherit Columns To Objects"

class ViewModelFormBcObjInheritInherits(ViewModelFormController):
	_name = "form:bc.obj.inherit.inherits"
	_view_name = "bc.obj.inherit.inherits/form"
	_description = "Inherit Columns To Objects"
