from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderTypeRoles(ViewModelFindController):
	_name = "find:crm.order.type.roles"
	_view_name = "crm.order.type.roles/find"
	_description = "Role Sale Order Types"

class ViewModelO2MFormCrmOrderTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.type.roles"
	_view_name = "crm.order.type.roles/o2m-form"
	_description = "Role Sale Order Types"

class ViewModelO2MListCrmOrderTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.order.type.roles"
	_view_name = "crm.order.type.roles/o2m-list"
	_description = "Role Sale Order Types"
