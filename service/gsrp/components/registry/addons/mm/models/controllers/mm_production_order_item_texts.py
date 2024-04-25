from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderItemTexts(ViewModelFindController):
	_name = "find:mm.production.order.item.texts"
	_view_name = "mm.production.order.item.texts/find"
	_description = "Production Order Item Texts"

class ViewModelO2MFormMmProductionOrderItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.item.texts"
	_view_name = "mm.production.order.item.texts/o2m-form"
	_description = "Production Order Item Texts"

class ViewModelO2MListMmProductionOrderItemTexts(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.item.texts"
	_view_name = "mm.production.order.item.texts/o2m-list"
	_description = "Production Order Item Texts"
