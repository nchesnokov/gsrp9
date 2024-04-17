from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchOilPlatformCategory(ViewModelSearchController):
	_name = "search:oil.platform.category"
	_view_name = "oil.platform.category/search"
	_description = "Platform Category"

class ViewModelFindOilPlatformCategory(ViewModelFindController):
	_name = "find:oil.platform.category"
	_view_name = "oil.platform.category/find"
	_description = "Platform Category"

class ViewModelListOilPlatformCategory(ViewModelListController):
	_name = "list:oil.platform.category"
	_view_name = "oil.platform.category/list"
	_description = "Platform Category"

class ViewModelFormModalOilPlatformCategory(ViewModelFormModalController):
	_name = "form.modal:oil.platform.category"
	_view_name = "oil.platform.category/form.modal"
	_description = "Platform Category"

class ViewModelFormOilPlatformCategory(ViewModelFormController):
	_name = "form:oil.platform.category"
	_view_name = "oil.platform.category/form"
	_description = "Platform Category"

class ViewModelTreeOilPlatformCategory(ViewModelTreeController):
	_name = "tree:oil.platform.category"
	_view_name = "oil.platform.category/tree"
	_description = "Platform Category"
