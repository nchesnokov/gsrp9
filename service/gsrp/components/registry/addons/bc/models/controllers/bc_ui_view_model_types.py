from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUiViewModelTypes(ViewModelSearchController):
	_name = "search:bc.ui.view.model.types"
	_view_name = "bc.ui.view.model.types/search"
	_description = "UI Type Of View"

class ViewModelFindBcUiViewModelTypes(ViewModelFindController):
	_name = "find:bc.ui.view.model.types"
	_view_name = "bc.ui.view.model.types/find"
	_description = "UI Type Of View"

class ViewModelListBcUiViewModelTypes(ViewModelListController):
	_name = "list:bc.ui.view.model.types"
	_view_name = "bc.ui.view.model.types/list"
	_description = "UI Type Of View"

class ViewModelFormModalBcUiViewModelTypes(ViewModelFormModalController):
	_name = "form.modal:bc.ui.view.model.types"
	_view_name = "bc.ui.view.model.types/form.modal"
	_description = "UI Type Of View"

class ViewModelFormBcUiViewModelTypes(ViewModelFormController):
	_name = "form:bc.ui.view.model.types"
	_view_name = "bc.ui.view.model.types/form"
	_description = "UI Type Of View"
