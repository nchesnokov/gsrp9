from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchOilPlatform(ViewModelSearchController):
	_name = "search:oil.platform"
	_view_name = "oil.platform/search"
	_description = "Platform"

class ViewModelFindOilPlatform(ViewModelFindController):
	_name = "find:oil.platform"
	_view_name = "oil.platform/find"
	_description = "Platform"

class ViewModelListOilPlatform(ViewModelListController):
	_name = "list:oil.platform"
	_view_name = "oil.platform/list"
	_description = "Platform"

class ViewModelFormModalOilPlatform(ViewModelFormModalController):
	_name = "form.modal:oil.platform"
	_view_name = "oil.platform/form.modal"
	_description = "Platform"

class ViewModelFormOilPlatform(ViewModelFormController):
	_name = "form:oil.platform"
	_view_name = "oil.platform/form"
	_description = "Platform"
