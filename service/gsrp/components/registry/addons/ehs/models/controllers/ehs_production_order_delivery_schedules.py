from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsProductionOrderDeliverySchedules(ViewModelFindController):
	_name = "find:ehs.production.order.delivery.schedules"
	_view_name = "ehs.production.order.delivery.schedules/find"
	_description = "Production Order Delivery Schedule"

class ViewModelO2MFormEhsProductionOrderDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:ehs.production.order.delivery.schedules"
	_view_name = "ehs.production.order.delivery.schedules/o2m-form"
	_description = "Production Order Delivery Schedule"

class ViewModelO2MListEhsProductionOrderDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:ehs.production.order.delivery.schedules"
	_view_name = "ehs.production.order.delivery.schedules/o2m-list"
	_description = "Production Order Delivery Schedule"
