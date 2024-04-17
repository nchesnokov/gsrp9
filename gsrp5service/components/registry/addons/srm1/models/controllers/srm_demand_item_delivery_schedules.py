from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.demand.item.delivery.schedules"
	_view_name = "srm.demand.item.delivery.schedules/find"
	_description = "SRM Demand Delivery Schedules"

class ViewModelO2MFormSrmDemandItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.item.delivery.schedules"
	_view_name = "srm.demand.item.delivery.schedules/o2m-form"
	_description = "SRM Demand Delivery Schedules"

class ViewModelO2MCalendarSrmDemandItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.demand.item.delivery.schedules"
	_view_name = "srm.demand.item.delivery.schedules/o2m-calendar"
	_description = "SRM Demand Delivery Schedules"

class ViewModelO2MGraphSrmDemandItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.demand.item.delivery.schedules"
	_view_name = "srm.demand.item.delivery.schedules/o2m-graph"
	_description = "SRM Demand Delivery Schedules"

class ViewModelO2MMdxSrmDemandItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.demand.item.delivery.schedules"
	_view_name = "srm.demand.item.delivery.schedules/o2m-mdx"
	_description = "SRM Demand Delivery Schedules"

class ViewModelO2MListSrmDemandItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.item.delivery.schedules"
	_view_name = "srm.demand.item.delivery.schedules/o2m-list"
	_description = "SRM Demand Delivery Schedules"
