from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.evolution.item.delivery.schedules"
	_view_name = "srm.evolution.item.delivery.schedules/find"
	_description = "SRM Evolution Delivery Schedules"

class ViewModelO2MFormSrmEvolutionItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.item.delivery.schedules"
	_view_name = "srm.evolution.item.delivery.schedules/o2m-form"
	_description = "SRM Evolution Delivery Schedules"

class ViewModelO2MCalendarSrmEvolutionItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.evolution.item.delivery.schedules"
	_view_name = "srm.evolution.item.delivery.schedules/o2m-calendar"
	_description = "SRM Evolution Delivery Schedules"

class ViewModelO2MGraphSrmEvolutionItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.evolution.item.delivery.schedules"
	_view_name = "srm.evolution.item.delivery.schedules/o2m-graph"
	_description = "SRM Evolution Delivery Schedules"

class ViewModelO2MMdxSrmEvolutionItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.evolution.item.delivery.schedules"
	_view_name = "srm.evolution.item.delivery.schedules/o2m-mdx"
	_description = "SRM Evolution Delivery Schedules"

class ViewModelO2MListSrmEvolutionItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.item.delivery.schedules"
	_view_name = "srm.evolution.item.delivery.schedules/o2m-list"
	_description = "SRM Evolution Delivery Schedules"
