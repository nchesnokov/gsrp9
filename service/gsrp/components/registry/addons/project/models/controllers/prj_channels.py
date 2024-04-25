from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjChannels(ViewModelSearchController):
	_name = "search:prj.channels"
	_view_name = "prj.channels/search"
	_description = "Project Channels"

class ViewModelFindPrjChannels(ViewModelFindController):
	_name = "find:prj.channels"
	_view_name = "prj.channels/find"
	_description = "Project Channels"

class ViewModelListPrjChannels(ViewModelListController):
	_name = "list:prj.channels"
	_view_name = "prj.channels/list"
	_description = "Project Channels"

class ViewModelFormModalPrjChannels(ViewModelFormModalController):
	_name = "form.modal:prj.channels"
	_view_name = "prj.channels/form.modal"
	_description = "Project Channels"

class ViewModelFormPrjChannels(ViewModelFormController):
	_name = "form:prj.channels"
	_view_name = "prj.channels/form"
	_description = "Project Channels"
