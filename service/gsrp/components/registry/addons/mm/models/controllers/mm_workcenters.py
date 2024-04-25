from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmWorkcenters(ViewModelSearchController):
	_name = "search:mm.workcenters"
	_view_name = "mm.workcenters/search"
	_description = "Workcenter"

class ViewModelFindMmWorkcenters(ViewModelFindController):
	_name = "find:mm.workcenters"
	_view_name = "mm.workcenters/find"
	_description = "Workcenter"

class ViewModelListMmWorkcenters(ViewModelListController):
	_name = "list:mm.workcenters"
	_view_name = "mm.workcenters/list"
	_description = "Workcenter"

class ViewModelFormModalMmWorkcenters(ViewModelFormModalController):
	_name = "form.modal:mm.workcenters"
	_view_name = "mm.workcenters/form.modal"
	_description = "Workcenter"

class ViewModelFormMmWorkcenters(ViewModelFormController):
	_name = "form:mm.workcenters"
	_view_name = "mm.workcenters/form"
	_description = "Workcenter"
