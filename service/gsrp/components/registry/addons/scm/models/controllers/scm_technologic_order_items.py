from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MTreeController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmTechnologicOrderItems(ViewModelFindController):
	_name = "find:scm.technologic.order.items"
	_view_name = "scm.technologic.order.items/find"
	_description = "Technologic Order Items"

class ViewModelO2MFormScmTechnologicOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:scm.technologic.order.items"
	_view_name = "scm.technologic.order.items/o2m-form"
	_description = "Technologic Order Items"

class ViewModelO2MTreeScmTechnologicOrderItems(ViewModelO2MTreeController):
	_name = "o2m-tree:scm.technologic.order.items"
	_view_name = "scm.technologic.order.items/o2m-tree"
	_description = "Technologic Order Items"

class ViewModelO2MListScmTechnologicOrderItems(ViewModelO2MListController):
	_name = "o2m-list:scm.technologic.order.items"
	_view_name = "scm.technologic.order.items/o2m-list"
	_description = "Technologic Order Items"
