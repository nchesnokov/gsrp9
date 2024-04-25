from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcModelInheritInherits(ViewModelSearchController):
	_name = "search:bc.model.inherit.inherits"
	_view_name = "bc.model.inherit.inherits/search"
	_description = "Inherit Columns To Models"

class ViewModelFindBcModelInheritInherits(ViewModelFindController):
	_name = "find:bc.model.inherit.inherits"
	_view_name = "bc.model.inherit.inherits/find"
	_description = "Inherit Columns To Models"

class ViewModelListBcModelInheritInherits(ViewModelListController):
	_name = "list:bc.model.inherit.inherits"
	_view_name = "bc.model.inherit.inherits/list"
	_description = "Inherit Columns To Models"

class ViewModelFormModalBcModelInheritInherits(ViewModelFormModalController):
	_name = "form.modal:bc.model.inherit.inherits"
	_view_name = "bc.model.inherit.inherits/form.modal"
	_description = "Inherit Columns To Models"

class ViewModelFormBcModelInheritInherits(ViewModelFormController):
	_name = "form:bc.model.inherit.inherits"
	_view_name = "bc.model.inherit.inherits/form"
	_description = "Inherit Columns To Models"
