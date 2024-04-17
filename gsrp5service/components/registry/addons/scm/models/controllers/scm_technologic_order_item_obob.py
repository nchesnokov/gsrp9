from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmTechnologicOrderItemObob(ViewModelFindController):
	_name = "find:scm.technologic.order.item.obob"
	_view_name = "scm.technologic.order.item.obob/find"
	_description = "Technologic Order Items OutBoB"

class ViewModelO2MFormScmTechnologicOrderItemObob(ViewModelO2MFormController):
	_name = "o2m-form:scm.technologic.order.item.obob"
	_view_name = "scm.technologic.order.item.obob/o2m-form"
	_description = "Technologic Order Items OutBoB"

class ViewModelO2MListScmTechnologicOrderItemObob(ViewModelO2MListController):
	_name = "o2m-list:scm.technologic.order.item.obob"
	_view_name = "scm.technologic.order.item.obob/o2m-list"
	_description = "Technologic Order Items OutBoB"
