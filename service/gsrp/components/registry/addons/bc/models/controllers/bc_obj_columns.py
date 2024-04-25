from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcObjColumns(ViewModelSearchController):
	_name = "search:bc.obj.columns"
	_view_name = "bc.obj.columns/search"
	_description = "Columns Of Model"

class ViewModelFindBcObjColumns(ViewModelFindController):
	_name = "find:bc.obj.columns"
	_view_name = "bc.obj.columns/find"
	_description = "Columns Of Model"

class ViewModelListBcObjColumns(ViewModelListController):
	_name = "list:bc.obj.columns"
	_view_name = "bc.obj.columns/list"
	_description = "Columns Of Model"

class ViewModelFormModalBcObjColumns(ViewModelFormModalController):
	_name = "form.modal:bc.obj.columns"
	_view_name = "bc.obj.columns/form.modal"
	_description = "Columns Of Model"

class ViewModelFormBcObjColumns(ViewModelFormController):
	_name = "form:bc.obj.columns"
	_view_name = "bc.obj.columns/form"
	_description = "Columns Of Model"
