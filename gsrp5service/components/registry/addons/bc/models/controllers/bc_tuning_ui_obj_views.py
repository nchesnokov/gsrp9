from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcTuningUiObjViews(ViewModelSearchController):
	_name = "search:bc.tuning.ui.obj.views"
	_view_name = "bc.tuning.ui.obj.views/search"
	_description = "Tunning Objects Views"

class ViewModelFindBcTuningUiObjViews(ViewModelFindController):
	_name = "find:bc.tuning.ui.obj.views"
	_view_name = "bc.tuning.ui.obj.views/find"
	_description = "Tunning Objects Views"

class ViewModelListBcTuningUiObjViews(ViewModelListController):
	_name = "list:bc.tuning.ui.obj.views"
	_view_name = "bc.tuning.ui.obj.views/list"
	_description = "Tunning Objects Views"

class ViewModelFormModalBcTuningUiObjViews(ViewModelFormModalController):
	_name = "form.modal:bc.tuning.ui.obj.views"
	_view_name = "bc.tuning.ui.obj.views/form.modal"
	_description = "Tunning Objects Views"

class ViewModelFormBcTuningUiObjViews(ViewModelFormController):
	_name = "form:bc.tuning.ui.obj.views"
	_view_name = "bc.tuning.ui.obj.views/form"
	_description = "Tunning Objects Views"
