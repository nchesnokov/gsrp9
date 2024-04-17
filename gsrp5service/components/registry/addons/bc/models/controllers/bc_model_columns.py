from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcModelColumns(ViewModelSearchController):
	_name = "search:bc.model.columns"
	_view_name = "bc.model.columns/search"
	_description = "Columns Of Model"

class ViewModelFindBcModelColumns(ViewModelFindController):
	_name = "find:bc.model.columns"
	_view_name = "bc.model.columns/find"
	_description = "Columns Of Model"

class ViewModelListBcModelColumns(ViewModelListController):
	_name = "list:bc.model.columns"
	_view_name = "bc.model.columns/list"
	_description = "Columns Of Model"

class ViewModelFormModalBcModelColumns(ViewModelFormModalController):
	_name = "form.modal:bc.model.columns"
	_view_name = "bc.model.columns/form.modal"
	_description = "Columns Of Model"

class ViewModelFormBcModelColumns(ViewModelFormController):
	_name = "form:bc.model.columns"
	_view_name = "bc.model.columns/form"
	_description = "Columns Of Model"
