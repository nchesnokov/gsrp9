from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.decision.item.delivery.schedules"
	_view_name = "srm.decision.item.delivery.schedules/find"
	_description = "SRM Decision Delivery Schedules"

class ViewModelO2MFormSrmDecisionItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.item.delivery.schedules"
	_view_name = "srm.decision.item.delivery.schedules/o2m-form"
	_description = "SRM Decision Delivery Schedules"

class ViewModelO2MCalendarSrmDecisionItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.decision.item.delivery.schedules"
	_view_name = "srm.decision.item.delivery.schedules/o2m-calendar"
	_description = "SRM Decision Delivery Schedules"

class ViewModelO2MGraphSrmDecisionItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.decision.item.delivery.schedules"
	_view_name = "srm.decision.item.delivery.schedules/o2m-graph"
	_description = "SRM Decision Delivery Schedules"

class ViewModelO2MMdxSrmDecisionItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.decision.item.delivery.schedules"
	_view_name = "srm.decision.item.delivery.schedules/o2m-mdx"
	_description = "SRM Decision Delivery Schedules"

class ViewModelO2MListSrmDecisionItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.item.delivery.schedules"
	_view_name = "srm.decision.item.delivery.schedules/o2m-list"
	_description = "SRM Decision Delivery Schedules"
