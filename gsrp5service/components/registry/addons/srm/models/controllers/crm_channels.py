from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmChannels(ViewModelSearchController):
	_name = "search:crm.channels"
	_view_name = "crm.channels/search"
	_description = "CRM Channels"

class ViewModelFindCrmChannels(ViewModelFindController):
	_name = "find:crm.channels"
	_view_name = "crm.channels/find"
	_description = "CRM Channels"

class ViewModelListCrmChannels(ViewModelListController):
	_name = "list:crm.channels"
	_view_name = "crm.channels/list"
	_description = "CRM Channels"

class ViewModelFormModalCrmChannels(ViewModelFormModalController):
	_name = "form.modal:crm.channels"
	_view_name = "crm.channels/form.modal"
	_description = "CRM Channels"

class ViewModelFormCrmChannels(ViewModelFormController):
	_name = "form:crm.channels"
	_view_name = "crm.channels/form"
	_description = "CRM Channels"
