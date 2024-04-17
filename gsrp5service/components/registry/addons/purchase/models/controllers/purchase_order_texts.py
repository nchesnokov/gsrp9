from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderTexts(ViewModelFindController):
	_name = "find:purchase.order.texts"
	_view_name = "purchase.order.texts/find"
	_description = "Purchase Order Texts"

class ViewModelO2MFormPurchaseOrderTexts(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.texts"
	_view_name = "purchase.order.texts/o2m-form"
	_description = "Purchase Order Texts"

class ViewModelO2MListPurchaseOrderTexts(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.texts"
	_view_name = "purchase.order.texts/o2m-list"
	_description = "Purchase Order Texts"
