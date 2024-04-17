from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUiObjViews(ViewModelSearchController):
	_name = "search:bc.ui.obj.views"
	_view_name = "bc.ui.obj.views/search"
	_description = "UI Views"

class ViewModelFindBcUiObjViews(ViewModelFindController):
	_name = "find:bc.ui.obj.views"
	_view_name = "bc.ui.obj.views/find"
	_description = "UI Views"

class ViewModelListBcUiObjViews(ViewModelListController):
	_name = "list:bc.ui.obj.views"
	_view_name = "bc.ui.obj.views/list"
	_description = "UI Views"

class ViewModelFormModalBcUiObjViews(ViewModelFormModalController):
	_name = "form.modal:bc.ui.obj.views"
	_view_name = "bc.ui.obj.views/form.modal"
	_description = "UI Views"

class ViewModelFormBcUiObjViews(ViewModelFormController):
	_name = "form:bc.ui.obj.views"
	_view_name = "bc.ui.obj.views/form"
	_description = "UI Views"
