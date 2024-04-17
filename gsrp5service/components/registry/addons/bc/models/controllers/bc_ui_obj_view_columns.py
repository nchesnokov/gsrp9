from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcUiObjViewColumns(ViewModelFindController):
	_name = "find:bc.ui.obj.view.columns"
	_view_name = "bc.ui.obj.view.columns/find"
	_description = "UI Objects View Columns"

class ViewModelO2MFormBcUiObjViewColumns(ViewModelO2MFormController):
	_name = "o2m-form:bc.ui.obj.view.columns"
	_view_name = "bc.ui.obj.view.columns/o2m-form"
	_description = "UI Objects View Columns"

class ViewModelO2MListBcUiObjViewColumns(ViewModelO2MListController):
	_name = "o2m-list:bc.ui.obj.view.columns"
	_view_name = "bc.ui.obj.view.columns/o2m-list"
	_description = "UI Objects View Columns"
