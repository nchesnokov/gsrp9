from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsTechnologicOrderDeliverySchedules(ViewModelFindController):
	_name = "find:ehs.technologic.order.delivery.schedules"
	_view_name = "ehs.technologic.order.delivery.schedules/find"
	_description = "Technologic Order Delivery Schedule"

class ViewModelO2MFormEhsTechnologicOrderDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:ehs.technologic.order.delivery.schedules"
	_view_name = "ehs.technologic.order.delivery.schedules/o2m-form"
	_description = "Technologic Order Delivery Schedule"

class ViewModelO2MListEhsTechnologicOrderDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:ehs.technologic.order.delivery.schedules"
	_view_name = "ehs.technologic.order.delivery.schedules/o2m-list"
	_description = "Technologic Order Delivery Schedule"
