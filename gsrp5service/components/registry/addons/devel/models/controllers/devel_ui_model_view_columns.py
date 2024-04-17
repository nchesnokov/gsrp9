from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindDevelUiModelViewColumns(ViewModelFindController):
	_name = "find:devel.ui.model.view.columns"
	_view_name = "devel.ui.model.view.columns/find"
	_description = "UI Model View Columns"

class ViewModelO2MFormDevelUiModelViewColumns(ViewModelO2MFormController):
	_name = "o2m-form:devel.ui.model.view.columns"
	_view_name = "devel.ui.model.view.columns/o2m-form"
	_description = "UI Model View Columns"

class ViewModelO2MListDevelUiModelViewColumns(ViewModelO2MListController):
	_name = "o2m-list:devel.ui.model.view.columns"
	_view_name = "devel.ui.model.view.columns/o2m-list"
	_description = "UI Model View Columns"
