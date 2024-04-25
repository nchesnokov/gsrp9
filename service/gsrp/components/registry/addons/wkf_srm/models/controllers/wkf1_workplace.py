from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchWkf1Workplace(ViewModelSearchController):
	_name = "search:wkf1.workplace"
	_view_name = "wkf1.workplace/search"
	_description = "Workflow Workplaces"

class ViewModelFindWkf1Workplace(ViewModelFindController):
	_name = "find:wkf1.workplace"
	_view_name = "wkf1.workplace/find"
	_description = "Workflow Workplaces"

class ViewModelListWkf1Workplace(ViewModelListController):
	_name = "list:wkf1.workplace"
	_view_name = "wkf1.workplace/list"
	_description = "Workflow Workplaces"

class ViewModelFormModalWkf1Workplace(ViewModelFormModalController):
	_name = "form.modal:wkf1.workplace"
	_view_name = "wkf1.workplace/form.modal"
	_description = "Workflow Workplaces"

class ViewModelFormWkf1Workplace(ViewModelFormController):
	_name = "form:wkf1.workplace"
	_view_name = "wkf1.workplace/form"
	_description = "Workflow Workplaces"
