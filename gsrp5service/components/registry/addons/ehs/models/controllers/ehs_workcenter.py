from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchEhsWorkcenter(ViewModelSearchController):
	_name = "search:ehs.workcenter"
	_view_name = "ehs.workcenter/search"
	_description = "Workcenter"

class ViewModelFindEhsWorkcenter(ViewModelFindController):
	_name = "find:ehs.workcenter"
	_view_name = "ehs.workcenter/find"
	_description = "Workcenter"

class ViewModelListEhsWorkcenter(ViewModelListController):
	_name = "list:ehs.workcenter"
	_view_name = "ehs.workcenter/list"
	_description = "Workcenter"

class ViewModelFormModalEhsWorkcenter(ViewModelFormModalController):
	_name = "form.modal:ehs.workcenter"
	_view_name = "ehs.workcenter/form.modal"
	_description = "Workcenter"

class ViewModelFormEhsWorkcenter(ViewModelFormController):
	_name = "form:ehs.workcenter"
	_view_name = "ehs.workcenter/form"
	_description = "Workcenter"
