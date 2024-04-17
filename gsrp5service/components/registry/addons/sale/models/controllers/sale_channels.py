from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleChannels(ViewModelSearchController):
	_name = "search:sale.channels"
	_view_name = "sale.channels/search"
	_description = "Sale Channels"

class ViewModelFindSaleChannels(ViewModelFindController):
	_name = "find:sale.channels"
	_view_name = "sale.channels/find"
	_description = "Sale Channels"

class ViewModelListSaleChannels(ViewModelListController):
	_name = "list:sale.channels"
	_view_name = "sale.channels/list"
	_description = "Sale Channels"

class ViewModelFormModalSaleChannels(ViewModelFormModalController):
	_name = "form.modal:sale.channels"
	_view_name = "sale.channels/form.modal"
	_description = "Sale Channels"

class ViewModelFormSaleChannels(ViewModelFormController):
	_name = "form:sale.channels"
	_view_name = "sale.channels/form"
	_description = "Sale Channels"
