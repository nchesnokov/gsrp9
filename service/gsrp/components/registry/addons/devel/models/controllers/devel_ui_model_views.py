from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchDevelUiModelViews(ViewModelSearchController):
	_name = "search:devel.ui.model.views"
	_view_name = "devel.ui.model.views/search"
	_description = "UI Views"

class ViewModelFindDevelUiModelViews(ViewModelFindController):
	_name = "find:devel.ui.model.views"
	_view_name = "devel.ui.model.views/find"
	_description = "UI Views"

class ViewModelListDevelUiModelViews(ViewModelListController):
	_name = "list:devel.ui.model.views"
	_view_name = "devel.ui.model.views/list"
	_description = "UI Views"

class ViewModelFormModalDevelUiModelViews(ViewModelFormModalController):
	_name = "form.modal:devel.ui.model.views"
	_view_name = "devel.ui.model.views/form.modal"
	_description = "UI Views"

class ViewModelFormDevelUiModelViews(ViewModelFormController):
	_name = "form:devel.ui.model.views"
	_view_name = "devel.ui.model.views/form"
	_description = "UI Views"
