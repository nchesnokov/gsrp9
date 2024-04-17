from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchDevelUiViewModelTypes(ViewModelSearchController):
	_name = "search:devel.ui.view.model.types"
	_view_name = "devel.ui.view.model.types/search"
	_description = "UI Type Of View"

class ViewModelFindDevelUiViewModelTypes(ViewModelFindController):
	_name = "find:devel.ui.view.model.types"
	_view_name = "devel.ui.view.model.types/find"
	_description = "UI Type Of View"

class ViewModelListDevelUiViewModelTypes(ViewModelListController):
	_name = "list:devel.ui.view.model.types"
	_view_name = "devel.ui.view.model.types/list"
	_description = "UI Type Of View"

class ViewModelFormModalDevelUiViewModelTypes(ViewModelFormModalController):
	_name = "form.modal:devel.ui.view.model.types"
	_view_name = "devel.ui.view.model.types/form.modal"
	_description = "UI Type Of View"

class ViewModelFormDevelUiViewModelTypes(ViewModelFormController):
	_name = "form:devel.ui.view.model.types"
	_view_name = "devel.ui.view.model.types/form"
	_description = "UI Type Of View"
