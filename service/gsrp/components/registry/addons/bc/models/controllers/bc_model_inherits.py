from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcModelInherits(ViewModelSearchController):
	_name = "search:bc.model.inherits"
	_view_name = "bc.model.inherits/search"
	_description = "Model Inherits"

class ViewModelFindBcModelInherits(ViewModelFindController):
	_name = "find:bc.model.inherits"
	_view_name = "bc.model.inherits/find"
	_description = "Model Inherits"

class ViewModelListBcModelInherits(ViewModelListController):
	_name = "list:bc.model.inherits"
	_view_name = "bc.model.inherits/list"
	_description = "Model Inherits"

class ViewModelFormModalBcModelInherits(ViewModelFormModalController):
	_name = "form.modal:bc.model.inherits"
	_view_name = "bc.model.inherits/form.modal"
	_description = "Model Inherits"

class ViewModelFormBcModelInherits(ViewModelFormController):
	_name = "form:bc.model.inherits"
	_view_name = "bc.model.inherits/form"
	_description = "Model Inherits"
