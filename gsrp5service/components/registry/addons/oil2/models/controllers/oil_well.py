from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchOilWell(ViewModelSearchController):
	_name = "search:oil.well"
	_view_name = "oil.well/search"
	_description = "Well"

class ViewModelFindOilWell(ViewModelFindController):
	_name = "find:oil.well"
	_view_name = "oil.well/find"
	_description = "Well"

class ViewModelListOilWell(ViewModelListController):
	_name = "list:oil.well"
	_view_name = "oil.well/list"
	_description = "Well"

class ViewModelFormModalOilWell(ViewModelFormModalController):
	_name = "form.modal:oil.well"
	_view_name = "oil.well/form.modal"
	_description = "Well"

class ViewModelFormOilWell(ViewModelFormController):
	_name = "form:oil.well"
	_view_name = "oil.well/form"
	_description = "Well"
