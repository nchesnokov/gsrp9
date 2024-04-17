from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUiFrameworkObjActions(ViewModelSearchController):
	_name = "search:bc.ui.framework.obj.actions"
	_view_name = "bc.ui.framework.obj.actions/search"
	_description = "Object UI Framework Actions"

class ViewModelFindBcUiFrameworkObjActions(ViewModelFindController):
	_name = "find:bc.ui.framework.obj.actions"
	_view_name = "bc.ui.framework.obj.actions/find"
	_description = "Object UI Framework Actions"

class ViewModelListBcUiFrameworkObjActions(ViewModelListController):
	_name = "list:bc.ui.framework.obj.actions"
	_view_name = "bc.ui.framework.obj.actions/list"
	_description = "Object UI Framework Actions"

class ViewModelFormModalBcUiFrameworkObjActions(ViewModelFormModalController):
	_name = "form.modal:bc.ui.framework.obj.actions"
	_view_name = "bc.ui.framework.obj.actions/form.modal"
	_description = "Object UI Framework Actions"

class ViewModelFormBcUiFrameworkObjActions(ViewModelFormController):
	_name = "form:bc.ui.framework.obj.actions"
	_view_name = "bc.ui.framework.obj.actions/form"
	_description = "Object UI Framework Actions"
