from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderItemTexts(ViewModelFindController):
	_name = "find:crm.order.item.texts"
	_view_name = "crm.order.item.texts/find"
	_description = "CRM Order Item Texts"

class ViewModelO2MFormCrmOrderItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.item.texts"
	_view_name = "crm.order.item.texts/o2m-form"
	_description = "CRM Order Item Texts"

class ViewModelO2MListCrmOrderItemTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.order.item.texts"
	_view_name = "crm.order.item.texts/o2m-list"
	_description = "CRM Order Item Texts"
