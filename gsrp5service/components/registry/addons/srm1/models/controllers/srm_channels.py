from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmChannels(ViewModelSearchController):
	_name = "search:srm.channels"
	_view_name = "srm.channels/search"
	_description = "SRM Channels"

class ViewModelFindSrmChannels(ViewModelFindController):
	_name = "find:srm.channels"
	_view_name = "srm.channels/find"
	_description = "SRM Channels"

class ViewModelListSrmChannels(ViewModelListController):
	_name = "list:srm.channels"
	_view_name = "srm.channels/list"
	_description = "SRM Channels"

class ViewModelFormModalSrmChannels(ViewModelFormModalController):
	_name = "form.modal:srm.channels"
	_view_name = "srm.channels/form.modal"
	_description = "SRM Channels"

class ViewModelFormSrmChannels(ViewModelFormController):
	_name = "form:srm.channels"
	_view_name = "srm.channels/form"
	_description = "SRM Channels"
