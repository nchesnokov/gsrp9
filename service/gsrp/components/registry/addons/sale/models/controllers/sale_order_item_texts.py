from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderItemTexts(ViewModelFindController):
	_name = "find:sale.order.item.texts"
	_view_name = "sale.order.item.texts/find"
	_description = "Sale Order Item Texts"

class ViewModelO2MFormSaleOrderItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.item.texts"
	_view_name = "sale.order.item.texts/o2m-form"
	_description = "Sale Order Item Texts"

class ViewModelO2MListSaleOrderItemTexts(ViewModelO2MListController):
	_name = "o2m-list:sale.order.item.texts"
	_view_name = "sale.order.item.texts/o2m-list"
	_description = "Sale Order Item Texts"
