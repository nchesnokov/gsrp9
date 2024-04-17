from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcModuleFiles(ViewModelSearchController):
	_name = "search:bc.module.files"
	_view_name = "bc.module.files/search"
	_description = "Module File"

class ViewModelFindBcModuleFiles(ViewModelFindController):
	_name = "find:bc.module.files"
	_view_name = "bc.module.files/find"
	_description = "Module File"

class ViewModelListBcModuleFiles(ViewModelListController):
	_name = "list:bc.module.files"
	_view_name = "bc.module.files/list"
	_description = "Module File"

class ViewModelFormModalBcModuleFiles(ViewModelFormModalController):
	_name = "form.modal:bc.module.files"
	_view_name = "bc.module.files/form.modal"
	_description = "Module File"

class ViewModelFormBcModuleFiles(ViewModelFormController):
	_name = "form:bc.module.files"
	_view_name = "bc.module.files/form"
	_description = "Module File"
