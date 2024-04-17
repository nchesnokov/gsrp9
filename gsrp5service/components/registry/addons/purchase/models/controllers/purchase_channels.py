from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseChannels(ViewModelSearchController):
	_name = "search:purchase.channels"
	_view_name = "purchase.channels/search"
	_description = "Purchase Channels"

class ViewModelFindPurchaseChannels(ViewModelFindController):
	_name = "find:purchase.channels"
	_view_name = "purchase.channels/find"
	_description = "Purchase Channels"

class ViewModelListPurchaseChannels(ViewModelListController):
	_name = "list:purchase.channels"
	_view_name = "purchase.channels/list"
	_description = "Purchase Channels"

class ViewModelFormModalPurchaseChannels(ViewModelFormModalController):
	_name = "form.modal:purchase.channels"
	_view_name = "purchase.channels/form.modal"
	_description = "Purchase Channels"

class ViewModelFormPurchaseChannels(ViewModelFormController):
	_name = "form:purchase.channels"
	_view_name = "purchase.channels/form"
	_description = "Purchase Channels"
