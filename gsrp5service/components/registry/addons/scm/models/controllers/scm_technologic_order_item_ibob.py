from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmTechnologicOrderItemIbob(ViewModelFindController):
	_name = "find:scm.technologic.order.item.ibob"
	_view_name = "scm.technologic.order.item.ibob/find"
	_description = "Technologic Order Items InBoB"

class ViewModelO2MFormScmTechnologicOrderItemIbob(ViewModelO2MFormController):
	_name = "o2m-form:scm.technologic.order.item.ibob"
	_view_name = "scm.technologic.order.item.ibob/o2m-form"
	_description = "Technologic Order Items InBoB"

class ViewModelO2MListScmTechnologicOrderItemIbob(ViewModelO2MListController):
	_name = "o2m-list:scm.technologic.order.item.ibob"
	_view_name = "scm.technologic.order.item.ibob/o2m-list"
	_description = "Technologic Order Items InBoB"
