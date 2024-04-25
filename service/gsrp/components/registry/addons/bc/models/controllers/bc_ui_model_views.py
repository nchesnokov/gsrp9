from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUiModelViews(ViewModelSearchController):
	_name = "search:bc.ui.model.views"
	_view_name = "bc.ui.model.views/search"
	_description = "UI Model Views"

class ViewModelFindBcUiModelViews(ViewModelFindController):
	_name = "find:bc.ui.model.views"
	_view_name = "bc.ui.model.views/find"
	_description = "UI Model Views"

class ViewModelListBcUiModelViews(ViewModelListController):
	_name = "list:bc.ui.model.views"
	_view_name = "bc.ui.model.views/list"
	_description = "UI Model Views"

class ViewModelFormModalBcUiModelViews(ViewModelFormModalController):
	_name = "form.modal:bc.ui.model.views"
	_view_name = "bc.ui.model.views/form.modal"
	_description = "UI Model Views"

class ViewModelFormBcUiModelViews(ViewModelFormController):
	_name = "form:bc.ui.model.views"
	_view_name = "bc.ui.model.views/form"
	_description = "UI Model Views"
