from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsTechnologicOrderItemObob(ViewModelFindController):
	_name = "find:ehs.technologic.order.item.obob"
	_view_name = "ehs.technologic.order.item.obob/find"
	_description = "Technologic Order Items OutBoB"

class ViewModelO2MFormEhsTechnologicOrderItemObob(ViewModelO2MFormController):
	_name = "o2m-form:ehs.technologic.order.item.obob"
	_view_name = "ehs.technologic.order.item.obob/o2m-form"
	_description = "Technologic Order Items OutBoB"

class ViewModelO2MListEhsTechnologicOrderItemObob(ViewModelO2MListController):
	_name = "o2m-list:ehs.technologic.order.item.obob"
	_view_name = "ehs.technologic.order.item.obob/o2m-list"
	_description = "Technologic Order Items OutBoB"
