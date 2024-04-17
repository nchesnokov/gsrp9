from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelKanbanController

class ViewModelSearchTmHandlings(ViewModelSearchController):
	_name = "search:tm.handlings"
	_view_name = "tm.handlings/search"
	_description = "Handlings"

class ViewModelFindTmHandlings(ViewModelFindController):
	_name = "find:tm.handlings"
	_view_name = "tm.handlings/find"
	_description = "Handlings"

class ViewModelListTmHandlings(ViewModelListController):
	_name = "list:tm.handlings"
	_view_name = "tm.handlings/list"
	_description = "Handlings"

class ViewModelFormModalTmHandlings(ViewModelFormModalController):
	_name = "form.modal:tm.handlings"
	_view_name = "tm.handlings/form.modal"
	_description = "Handlings"

class ViewModelFormTmHandlings(ViewModelFormController):
	_name = "form:tm.handlings"
	_view_name = "tm.handlings/form"
	_description = "Handlings"

class ViewModelKanbanTmHandlings(ViewModelKanbanController):
	_name = "kanban:tm.handlings"
	_view_name = "tm.handlings/kanban"
	_description = "Handlings"
