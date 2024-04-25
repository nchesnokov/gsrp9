from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchOilWellCategory(ViewModelSearchController):
	_name = "search:oil.well.category"
	_view_name = "oil.well.category/search"
	_description = "Well Category"

class ViewModelFindOilWellCategory(ViewModelFindController):
	_name = "find:oil.well.category"
	_view_name = "oil.well.category/find"
	_description = "Well Category"

class ViewModelListOilWellCategory(ViewModelListController):
	_name = "list:oil.well.category"
	_view_name = "oil.well.category/list"
	_description = "Well Category"

class ViewModelFormModalOilWellCategory(ViewModelFormModalController):
	_name = "form.modal:oil.well.category"
	_view_name = "oil.well.category/form.modal"
	_description = "Well Category"

class ViewModelFormOilWellCategory(ViewModelFormController):
	_name = "form:oil.well.category"
	_view_name = "oil.well.category/form"
	_description = "Well Category"

class ViewModelTreeOilWellCategory(ViewModelTreeController):
	_name = "tree:oil.well.category"
	_view_name = "oil.well.category/tree"
	_description = "Well Category"
