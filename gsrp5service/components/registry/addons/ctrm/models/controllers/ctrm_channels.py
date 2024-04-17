from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmChannels(ViewModelSearchController):
	_name = "search:ctrm.channels"
	_view_name = "ctrm.channels/search"
	_description = "CTRM Cannels"

class ViewModelFindCtrmChannels(ViewModelFindController):
	_name = "find:ctrm.channels"
	_view_name = "ctrm.channels/find"
	_description = "CTRM Cannels"

class ViewModelListCtrmChannels(ViewModelListController):
	_name = "list:ctrm.channels"
	_view_name = "ctrm.channels/list"
	_description = "CTRM Cannels"

class ViewModelFormModalCtrmChannels(ViewModelFormModalController):
	_name = "form.modal:ctrm.channels"
	_view_name = "ctrm.channels/form.modal"
	_description = "CTRM Cannels"

class ViewModelFormCtrmChannels(ViewModelFormController):
	_name = "form:ctrm.channels"
	_view_name = "ctrm.channels/form"
	_description = "CTRM Cannels"
