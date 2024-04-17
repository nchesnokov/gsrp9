from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderItemObobTexts(ViewModelFindController):
	_name = "find:mm.technologic.order.item.obob.texts"
	_view_name = "mm.technologic.order.item.obob.texts/find"
	_description = "Technologic Order Output Item Texts"

class ViewModelO2MFormMmTechnologicOrderItemObobTexts(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.item.obob.texts"
	_view_name = "mm.technologic.order.item.obob.texts/o2m-form"
	_description = "Technologic Order Output Item Texts"

class ViewModelO2MListMmTechnologicOrderItemObobTexts(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.item.obob.texts"
	_view_name = "mm.technologic.order.item.obob.texts/o2m-list"
	_description = "Technologic Order Output Item Texts"
