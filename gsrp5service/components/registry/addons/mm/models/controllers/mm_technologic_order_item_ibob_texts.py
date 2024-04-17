from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderItemIbobTexts(ViewModelFindController):
	_name = "find:mm.technologic.order.item.ibob.texts"
	_view_name = "mm.technologic.order.item.ibob.texts/find"
	_description = "Technologic Order Input Item Texts"

class ViewModelO2MFormMmTechnologicOrderItemIbobTexts(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.item.ibob.texts"
	_view_name = "mm.technologic.order.item.ibob.texts/o2m-form"
	_description = "Technologic Order Input Item Texts"

class ViewModelO2MListMmTechnologicOrderItemIbobTexts(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.item.ibob.texts"
	_view_name = "mm.technologic.order.item.ibob.texts/o2m-list"
	_description = "Technologic Order Input Item Texts"
