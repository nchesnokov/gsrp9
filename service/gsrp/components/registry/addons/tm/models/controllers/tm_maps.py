from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelKanbanController

class ViewModelSearchTmMaps(ViewModelSearchController):
	_name = "search:tm.maps"
	_view_name = "tm.maps/search"
	_description = "Maps"

class ViewModelFindTmMaps(ViewModelFindController):
	_name = "find:tm.maps"
	_view_name = "tm.maps/find"
	_description = "Maps"

class ViewModelListTmMaps(ViewModelListController):
	_name = "list:tm.maps"
	_view_name = "tm.maps/list"
	_description = "Maps"

class ViewModelFormModalTmMaps(ViewModelFormModalController):
	_name = "form.modal:tm.maps"
	_view_name = "tm.maps/form.modal"
	_description = "Maps"

class ViewModelFormTmMaps(ViewModelFormController):
	_name = "form:tm.maps"
	_view_name = "tm.maps/form"
	_description = "Maps"

class ViewModelKanbanTmMaps(ViewModelKanbanController):
	_name = "kanban:tm.maps"
	_view_name = "tm.maps/kanban"
	_description = "Maps"
