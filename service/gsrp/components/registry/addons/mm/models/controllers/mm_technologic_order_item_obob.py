from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderItemObob(ViewModelFindController):
	_name = "find:mm.technologic.order.item.obob"
	_view_name = "mm.technologic.order.item.obob/find"
	_description = "Technologic Order Items OutBoB"

class ViewModelO2MFormMmTechnologicOrderItemObob(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.item.obob"
	_view_name = "mm.technologic.order.item.obob/o2m-form"
	_description = "Technologic Order Items OutBoB"

class ViewModelO2MListMmTechnologicOrderItemObob(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.item.obob"
	_view_name = "mm.technologic.order.item.obob/o2m-list"
	_description = "Technologic Order Items OutBoB"
