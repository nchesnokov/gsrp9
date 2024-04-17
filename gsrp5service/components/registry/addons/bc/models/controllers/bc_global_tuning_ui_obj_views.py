from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcGlobalTuningUiObjViews(ViewModelSearchController):
	_name = "search:bc.global.tuning.ui.obj.views"
	_view_name = "bc.global.tuning.ui.obj.views/search"
	_description = "Global Tunning Objct Views"

class ViewModelFindBcGlobalTuningUiObjViews(ViewModelFindController):
	_name = "find:bc.global.tuning.ui.obj.views"
	_view_name = "bc.global.tuning.ui.obj.views/find"
	_description = "Global Tunning Objct Views"

class ViewModelListBcGlobalTuningUiObjViews(ViewModelListController):
	_name = "list:bc.global.tuning.ui.obj.views"
	_view_name = "bc.global.tuning.ui.obj.views/list"
	_description = "Global Tunning Objct Views"

class ViewModelFormModalBcGlobalTuningUiObjViews(ViewModelFormModalController):
	_name = "form.modal:bc.global.tuning.ui.obj.views"
	_view_name = "bc.global.tuning.ui.obj.views/form.modal"
	_description = "Global Tunning Objct Views"

class ViewModelFormBcGlobalTuningUiObjViews(ViewModelFormController):
	_name = "form:bc.global.tuning.ui.obj.views"
	_view_name = "bc.global.tuning.ui.obj.views/form"
	_description = "Global Tunning Objct Views"
