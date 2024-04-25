from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderItemTexts(ViewModelFindController):
	_name = "find:purchase.order.item.texts"
	_view_name = "purchase.order.item.texts/find"
	_description = "Purchase Order Item Texts"

class ViewModelO2MFormPurchaseOrderItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.item.texts"
	_view_name = "purchase.order.item.texts/o2m-form"
	_description = "Purchase Order Item Texts"

class ViewModelO2MListPurchaseOrderItemTexts(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.item.texts"
	_view_name = "purchase.order.item.texts/o2m-list"
	_description = "Purchase Order Item Texts"
