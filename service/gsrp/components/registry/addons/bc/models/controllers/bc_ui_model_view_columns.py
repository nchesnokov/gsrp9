from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcUiModelViewColumns(ViewModelFindController):
	_name = "find:bc.ui.model.view.columns"
	_view_name = "bc.ui.model.view.columns/find"
	_description = "UI Model View Columns"

class ViewModelO2MFormBcUiModelViewColumns(ViewModelO2MFormController):
	_name = "o2m-form:bc.ui.model.view.columns"
	_view_name = "bc.ui.model.view.columns/o2m-form"
	_description = "UI Model View Columns"

class ViewModelO2MListBcUiModelViewColumns(ViewModelO2MListController):
	_name = "o2m-list:bc.ui.model.view.columns"
	_view_name = "bc.ui.model.view.columns/o2m-list"
	_description = "UI Model View Columns"
