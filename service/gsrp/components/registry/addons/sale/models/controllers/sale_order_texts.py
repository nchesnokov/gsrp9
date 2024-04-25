from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderTexts(ViewModelFindController):
	_name = "find:sale.order.texts"
	_view_name = "sale.order.texts/find"
	_description = "Sale Order Texts"

class ViewModelO2MFormSaleOrderTexts(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.texts"
	_view_name = "sale.order.texts/o2m-form"
	_description = "Sale Order Texts"

class ViewModelO2MListSaleOrderTexts(ViewModelO2MListController):
	_name = "o2m-list:sale.order.texts"
	_view_name = "sale.order.texts/o2m-list"
	_description = "Sale Order Texts"
