from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmProductionOrderDeliverySchedules(ViewModelFindController):
	_name = "find:scm.production.order.delivery.schedules"
	_view_name = "scm.production.order.delivery.schedules/find"
	_description = "Production Order Delivery Schedule"

class ViewModelO2MFormScmProductionOrderDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:scm.production.order.delivery.schedules"
	_view_name = "scm.production.order.delivery.schedules/o2m-form"
	_description = "Production Order Delivery Schedule"

class ViewModelO2MListScmProductionOrderDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:scm.production.order.delivery.schedules"
	_view_name = "scm.production.order.delivery.schedules/o2m-list"
	_description = "Production Order Delivery Schedule"
