from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderTypeItems(ViewModelFindController):
	_name = "find:crm.order.type.items"
	_view_name = "crm.order.type.items/find"
	_description = "Role CRM Order Items"

class ViewModelO2MFormCrmOrderTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.type.items"
	_view_name = "crm.order.type.items/o2m-form"
	_description = "Role CRM Order Items"

class ViewModelO2MListCrmOrderTypeItems(ViewModelO2MListController):
	_name = "o2m-list:crm.order.type.items"
	_view_name = "crm.order.type.items/o2m-list"
	_description = "Role CRM Order Items"
