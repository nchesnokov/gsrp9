from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchOilField(ViewModelSearchController):
	_name = "search:oil.field"
	_view_name = "oil.field/search"
	_description = "Field"

class ViewModelFindOilField(ViewModelFindController):
	_name = "find:oil.field"
	_view_name = "oil.field/find"
	_description = "Field"

class ViewModelListOilField(ViewModelListController):
	_name = "list:oil.field"
	_view_name = "oil.field/list"
	_description = "Field"

class ViewModelFormModalOilField(ViewModelFormModalController):
	_name = "form.modal:oil.field"
	_view_name = "oil.field/form.modal"
	_description = "Field"

class ViewModelFormOilField(ViewModelFormController):
	_name = "form:oil.field"
	_view_name = "oil.field/form"
	_description = "Field"
