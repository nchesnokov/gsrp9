from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderTexts(ViewModelFindController):
	_name = "find:mm.production.order.texts"
	_view_name = "mm.production.order.texts/find"
	_description = "Production Order Texts"

class ViewModelO2MFormMmProductionOrderTexts(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.texts"
	_view_name = "mm.production.order.texts/o2m-form"
	_description = "Production Order Texts"

class ViewModelO2MListMmProductionOrderTexts(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.texts"
	_view_name = "mm.production.order.texts/o2m-list"
	_description = "Production Order Texts"
