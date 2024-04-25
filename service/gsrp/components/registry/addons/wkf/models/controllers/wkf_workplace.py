from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchWkfWorkplace(ViewModelSearchController):
	_name = "search:wkf.workplace"
	_view_name = "wkf.workplace/search"
	_description = "Workflow Workplaces"

class ViewModelFindWkfWorkplace(ViewModelFindController):
	_name = "find:wkf.workplace"
	_view_name = "wkf.workplace/find"
	_description = "Workflow Workplaces"

class ViewModelListWkfWorkplace(ViewModelListController):
	_name = "list:wkf.workplace"
	_view_name = "wkf.workplace/list"
	_description = "Workflow Workplaces"

class ViewModelFormModalWkfWorkplace(ViewModelFormModalController):
	_name = "form.modal:wkf.workplace"
	_view_name = "wkf.workplace/form.modal"
	_description = "Workflow Workplaces"

class ViewModelFormWkfWorkplace(ViewModelFormController):
	_name = "form:wkf.workplace"
	_view_name = "wkf.workplace/form"
	_description = "Workflow Workplaces"
