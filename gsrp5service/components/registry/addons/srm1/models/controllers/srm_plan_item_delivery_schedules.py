from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.plan.item.delivery.schedules"
	_view_name = "srm.plan.item.delivery.schedules/find"
	_description = "SRM Plan Delivery Schedules"

class ViewModelO2MFormSrmPlanItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.item.delivery.schedules"
	_view_name = "srm.plan.item.delivery.schedules/o2m-form"
	_description = "SRM Plan Delivery Schedules"

class ViewModelO2MCalendarSrmPlanItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.plan.item.delivery.schedules"
	_view_name = "srm.plan.item.delivery.schedules/o2m-calendar"
	_description = "SRM Plan Delivery Schedules"

class ViewModelO2MGraphSrmPlanItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.plan.item.delivery.schedules"
	_view_name = "srm.plan.item.delivery.schedules/o2m-graph"
	_description = "SRM Plan Delivery Schedules"

class ViewModelO2MMdxSrmPlanItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.plan.item.delivery.schedules"
	_view_name = "srm.plan.item.delivery.schedules/o2m-mdx"
	_description = "SRM Plan Delivery Schedules"

class ViewModelO2MListSrmPlanItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.item.delivery.schedules"
	_view_name = "srm.plan.item.delivery.schedules/o2m-list"
	_description = "SRM Plan Delivery Schedules"
