from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchScmWorkcenter(ViewModelSearchController):
	_name = "search:scm.workcenter"
	_view_name = "scm.workcenter/search"
	_description = "Workcenter"

class ViewModelFindScmWorkcenter(ViewModelFindController):
	_name = "find:scm.workcenter"
	_view_name = "scm.workcenter/find"
	_description = "Workcenter"

class ViewModelListScmWorkcenter(ViewModelListController):
	_name = "list:scm.workcenter"
	_view_name = "scm.workcenter/list"
	_description = "Workcenter"

class ViewModelFormModalScmWorkcenter(ViewModelFormModalController):
	_name = "form.modal:scm.workcenter"
	_view_name = "scm.workcenter/form.modal"
	_description = "Workcenter"

class ViewModelFormScmWorkcenter(ViewModelFormController):
	_name = "form:scm.workcenter"
	_view_name = "scm.workcenter/form"
	_description = "Workcenter"
