from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcModelInheritColumns(ViewModelSearchController):
	_name = "search:bc.model.inherit.columns"
	_view_name = "bc.model.inherit.columns/search"
	_description = "Models Columns Inherits"

class ViewModelFindBcModelInheritColumns(ViewModelFindController):
	_name = "find:bc.model.inherit.columns"
	_view_name = "bc.model.inherit.columns/find"
	_description = "Models Columns Inherits"

class ViewModelListBcModelInheritColumns(ViewModelListController):
	_name = "list:bc.model.inherit.columns"
	_view_name = "bc.model.inherit.columns/list"
	_description = "Models Columns Inherits"

class ViewModelFormModalBcModelInheritColumns(ViewModelFormModalController):
	_name = "form.modal:bc.model.inherit.columns"
	_view_name = "bc.model.inherit.columns/form.modal"
	_description = "Models Columns Inherits"

class ViewModelFormBcModelInheritColumns(ViewModelFormController):
	_name = "form:bc.model.inherit.columns"
	_view_name = "bc.model.inherit.columns/form"
	_description = "Models Columns Inherits"
