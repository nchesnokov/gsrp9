from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmTechnologicOrderDeliverySchedules(ViewModelFindController):
	_name = "find:scm.technologic.order.delivery.schedules"
	_view_name = "scm.technologic.order.delivery.schedules/find"
	_description = "Technologic Order Delivery Schedule"

class ViewModelO2MFormScmTechnologicOrderDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:scm.technologic.order.delivery.schedules"
	_view_name = "scm.technologic.order.delivery.schedules/o2m-form"
	_description = "Technologic Order Delivery Schedule"

class ViewModelO2MListScmTechnologicOrderDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:scm.technologic.order.delivery.schedules"
	_view_name = "scm.technologic.order.delivery.schedules/o2m-list"
	_description = "Technologic Order Delivery Schedule"
