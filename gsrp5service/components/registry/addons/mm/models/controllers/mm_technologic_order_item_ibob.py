from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderItemIbob(ViewModelFindController):
	_name = "find:mm.technologic.order.item.ibob"
	_view_name = "mm.technologic.order.item.ibob/find"
	_description = "Technologic Order Items InBoB"

class ViewModelO2MFormMmTechnologicOrderItemIbob(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.item.ibob"
	_view_name = "mm.technologic.order.item.ibob/o2m-form"
	_description = "Technologic Order Items InBoB"

class ViewModelO2MListMmTechnologicOrderItemIbob(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.item.ibob"
	_view_name = "mm.technologic.order.item.ibob/o2m-list"
	_description = "Technologic Order Items InBoB"
