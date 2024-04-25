from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MTreeController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsTechnologicOrderItems(ViewModelFindController):
	_name = "find:ehs.technologic.order.items"
	_view_name = "ehs.technologic.order.items/find"
	_description = "Technologic Order Items"

class ViewModelO2MFormEhsTechnologicOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:ehs.technologic.order.items"
	_view_name = "ehs.technologic.order.items/o2m-form"
	_description = "Technologic Order Items"

class ViewModelO2MTreeEhsTechnologicOrderItems(ViewModelO2MTreeController):
	_name = "o2m-tree:ehs.technologic.order.items"
	_view_name = "ehs.technologic.order.items/o2m-tree"
	_description = "Technologic Order Items"

class ViewModelO2MListEhsTechnologicOrderItems(ViewModelO2MListController):
	_name = "o2m-list:ehs.technologic.order.items"
	_view_name = "ehs.technologic.order.items/o2m-list"
	_description = "Technologic Order Items"
