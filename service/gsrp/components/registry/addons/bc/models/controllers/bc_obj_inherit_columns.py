from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcObjInheritColumns(ViewModelSearchController):
	_name = "search:bc.obj.inherit.columns"
	_view_name = "bc.obj.inherit.columns/search"
	_description = "Objects Columns Inherits"

class ViewModelFindBcObjInheritColumns(ViewModelFindController):
	_name = "find:bc.obj.inherit.columns"
	_view_name = "bc.obj.inherit.columns/find"
	_description = "Objects Columns Inherits"

class ViewModelListBcObjInheritColumns(ViewModelListController):
	_name = "list:bc.obj.inherit.columns"
	_view_name = "bc.obj.inherit.columns/list"
	_description = "Objects Columns Inherits"

class ViewModelFormModalBcObjInheritColumns(ViewModelFormModalController):
	_name = "form.modal:bc.obj.inherit.columns"
	_view_name = "bc.obj.inherit.columns/form.modal"
	_description = "Objects Columns Inherits"

class ViewModelFormBcObjInheritColumns(ViewModelFormController):
	_name = "form:bc.obj.inherit.columns"
	_view_name = "bc.obj.inherit.columns/form"
	_description = "Objects Columns Inherits"
