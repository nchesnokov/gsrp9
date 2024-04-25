from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUiViewObjTypes(ViewModelSearchController):
	_name = "search:bc.ui.view.obj.types"
	_view_name = "bc.ui.view.obj.types/search"
	_description = "UI Type Of View"

class ViewModelFindBcUiViewObjTypes(ViewModelFindController):
	_name = "find:bc.ui.view.obj.types"
	_view_name = "bc.ui.view.obj.types/find"
	_description = "UI Type Of View"

class ViewModelListBcUiViewObjTypes(ViewModelListController):
	_name = "list:bc.ui.view.obj.types"
	_view_name = "bc.ui.view.obj.types/list"
	_description = "UI Type Of View"

class ViewModelFormModalBcUiViewObjTypes(ViewModelFormModalController):
	_name = "form.modal:bc.ui.view.obj.types"
	_view_name = "bc.ui.view.obj.types/form.modal"
	_description = "UI Type Of View"

class ViewModelFormBcUiViewObjTypes(ViewModelFormController):
	_name = "form:bc.ui.view.obj.types"
	_view_name = "bc.ui.view.obj.types/form"
	_description = "UI Type Of View"
