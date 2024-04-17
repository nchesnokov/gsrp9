from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderItems(ViewModelFindController):
	_name = "find:crm.order.items"
	_view_name = "crm.order.items/find"
	_description = "CRM Order Items"

class ViewModelO2MFormCrmOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.items"
	_view_name = "crm.order.items/o2m-form"
	_description = "CRM Order Items"

class ViewModelO2MListCrmOrderItems(ViewModelO2MListController):
	_name = "o2m-list:crm.order.items"
	_view_name = "crm.order.items/o2m-list"
	_description = "CRM Order Items"
