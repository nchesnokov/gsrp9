from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelKanbanController

class ViewModelSearchBcModules(ViewModelSearchController):
	_name = "search:bc.modules"
	_view_name = "bc.modules/search"
	_description = "Modules"

class ViewModelFindBcModules(ViewModelFindController):
	_name = "find:bc.modules"
	_view_name = "bc.modules/find"
	_description = "Modules"

class ViewModelListBcModules(ViewModelListController):
	_name = "list:bc.modules"
	_view_name = "bc.modules/list"
	_description = "Modules"

class ViewModelFormModalBcModules(ViewModelFormModalController):
	_name = "form.modal:bc.modules"
	_view_name = "bc.modules/form.modal"
	_description = "Modules"

class ViewModelFormBcModules(ViewModelFormController):
	_name = "form:bc.modules"
	_view_name = "bc.modules/form"
	_description = "Modules"

class ViewModelKanbanBcModules(ViewModelKanbanController):
	_name = "kanban:bc.modules"
	_view_name = "bc.modules/kanban"
	_description = "Modules"
