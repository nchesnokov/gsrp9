from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderTexts(ViewModelFindController):
	_name = "find:crm.order.texts"
	_view_name = "crm.order.texts/find"
	_description = "CRM Order Texts"

class ViewModelO2MFormCrmOrderTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.texts"
	_view_name = "crm.order.texts/o2m-form"
	_description = "CRM Order Texts"

class ViewModelO2MListCrmOrderTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.order.texts"
	_view_name = "crm.order.texts/o2m-list"
	_description = "CRM Order Texts"
