from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderSchedules(ViewModelFindController):
	_name = "find:mm.technologic.order.schedules"
	_view_name = "mm.technologic.order.schedules/find"
	_description = "Technologic Order Delivery Schedule"

class ViewModelO2MFormMmTechnologicOrderSchedules(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.schedules"
	_view_name = "mm.technologic.order.schedules/o2m-form"
	_description = "Technologic Order Delivery Schedule"

class ViewModelO2MListMmTechnologicOrderSchedules(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.schedules"
	_view_name = "mm.technologic.order.schedules/o2m-list"
	_description = "Technologic Order Delivery Schedule"
