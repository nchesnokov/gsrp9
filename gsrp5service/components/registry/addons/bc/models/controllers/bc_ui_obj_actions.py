from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUiObjActions(ViewModelSearchController):
	_name = "search:bc.ui.obj.actions"
	_view_name = "bc.ui.obj.actions/search"
	_description = "Object UI Actions"

class ViewModelFindBcUiObjActions(ViewModelFindController):
	_name = "find:bc.ui.obj.actions"
	_view_name = "bc.ui.obj.actions/find"
	_description = "Object UI Actions"

class ViewModelListBcUiObjActions(ViewModelListController):
	_name = "list:bc.ui.obj.actions"
	_view_name = "bc.ui.obj.actions/list"
	_description = "Object UI Actions"

class ViewModelFormModalBcUiObjActions(ViewModelFormModalController):
	_name = "form.modal:bc.ui.obj.actions"
	_view_name = "bc.ui.obj.actions/form.modal"
	_description = "Object UI Actions"

class ViewModelFormBcUiObjActions(ViewModelFormController):
	_name = "form:bc.ui.obj.actions"
	_view_name = "bc.ui.obj.actions/form"
	_description = "Object UI Actions"
