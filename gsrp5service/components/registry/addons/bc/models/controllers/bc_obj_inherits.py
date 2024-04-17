from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcObjInherits(ViewModelSearchController):
	_name = "search:bc.obj.inherits"
	_view_name = "bc.obj.inherits/search"
	_description = "Object Inherits"

class ViewModelFindBcObjInherits(ViewModelFindController):
	_name = "find:bc.obj.inherits"
	_view_name = "bc.obj.inherits/find"
	_description = "Object Inherits"

class ViewModelListBcObjInherits(ViewModelListController):
	_name = "list:bc.obj.inherits"
	_view_name = "bc.obj.inherits/list"
	_description = "Object Inherits"

class ViewModelFormModalBcObjInherits(ViewModelFormModalController):
	_name = "form.modal:bc.obj.inherits"
	_view_name = "bc.obj.inherits/form.modal"
	_description = "Object Inherits"

class ViewModelFormBcObjInherits(ViewModelFormController):
	_name = "form:bc.obj.inherits"
	_view_name = "bc.obj.inherits/form"
	_description = "Object Inherits"
