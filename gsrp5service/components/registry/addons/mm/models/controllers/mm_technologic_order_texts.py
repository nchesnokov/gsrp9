from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderTexts(ViewModelFindController):
	_name = "find:mm.technologic.order.texts"
	_view_name = "mm.technologic.order.texts/find"
	_description = "Technologic Order Texts"

class ViewModelO2MFormMmTechnologicOrderTexts(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.texts"
	_view_name = "mm.technologic.order.texts/o2m-form"
	_description = "Technologic Order Texts"

class ViewModelO2MListMmTechnologicOrderTexts(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.texts"
	_view_name = "mm.technologic.order.texts/o2m-list"
	_description = "Technologic Order Texts"
