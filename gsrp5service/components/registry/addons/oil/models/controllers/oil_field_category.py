from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchOilFieldCategory(ViewModelSearchController):
	_name = "search:oil.field.category"
	_view_name = "oil.field.category/search"
	_description = "Field Category"

class ViewModelFindOilFieldCategory(ViewModelFindController):
	_name = "find:oil.field.category"
	_view_name = "oil.field.category/find"
	_description = "Field Category"

class ViewModelListOilFieldCategory(ViewModelListController):
	_name = "list:oil.field.category"
	_view_name = "oil.field.category/list"
	_description = "Field Category"

class ViewModelFormModalOilFieldCategory(ViewModelFormModalController):
	_name = "form.modal:oil.field.category"
	_view_name = "oil.field.category/form.modal"
	_description = "Field Category"

class ViewModelFormOilFieldCategory(ViewModelFormController):
	_name = "form:oil.field.category"
	_view_name = "oil.field.category/form"
	_description = "Field Category"

class ViewModelTreeOilFieldCategory(ViewModelTreeController):
	_name = "tree:oil.field.category"
	_view_name = "oil.field.category/tree"
	_description = "Field Category"
