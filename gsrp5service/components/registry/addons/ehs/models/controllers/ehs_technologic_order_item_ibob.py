from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsTechnologicOrderItemIbob(ViewModelFindController):
	_name = "find:ehs.technologic.order.item.ibob"
	_view_name = "ehs.technologic.order.item.ibob/find"
	_description = "Technologic Order Items InBoB"

class ViewModelO2MFormEhsTechnologicOrderItemIbob(ViewModelO2MFormController):
	_name = "o2m-form:ehs.technologic.order.item.ibob"
	_view_name = "ehs.technologic.order.item.ibob/o2m-form"
	_description = "Technologic Order Items InBoB"

class ViewModelO2MListEhsTechnologicOrderItemIbob(ViewModelO2MListController):
	_name = "o2m-list:ehs.technologic.order.item.ibob"
	_view_name = "ehs.technologic.order.item.ibob/o2m-list"
	_description = "Technologic Order Items InBoB"
