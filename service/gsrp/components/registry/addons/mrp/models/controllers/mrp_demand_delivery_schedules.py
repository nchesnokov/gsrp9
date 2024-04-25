from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpDemandDeliverySchedules(ViewModelFindController):
	_name = "find:mrp.demand.delivery.schedules"
	_view_name = "mrp.demand.delivery.schedules/find"
	_description = "MRP Demand Delivery Schedule"

class ViewModelO2MFormMrpDemandDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:mrp.demand.delivery.schedules"
	_view_name = "mrp.demand.delivery.schedules/o2m-form"
	_description = "MRP Demand Delivery Schedule"

class ViewModelO2MListMrpDemandDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:mrp.demand.delivery.schedules"
	_view_name = "mrp.demand.delivery.schedules/o2m-list"
	_description = "MRP Demand Delivery Schedule"
