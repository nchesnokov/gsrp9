from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.contract.item.delivery.schedules"
	_view_name = "srm.contract.item.delivery.schedules/find"
	_description = "SRM Contract Delivery Schedules"

class ViewModelO2MFormSrmContractItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.item.delivery.schedules"
	_view_name = "srm.contract.item.delivery.schedules/o2m-form"
	_description = "SRM Contract Delivery Schedules"

class ViewModelO2MCalendarSrmContractItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.contract.item.delivery.schedules"
	_view_name = "srm.contract.item.delivery.schedules/o2m-calendar"
	_description = "SRM Contract Delivery Schedules"

class ViewModelO2MGraphSrmContractItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.contract.item.delivery.schedules"
	_view_name = "srm.contract.item.delivery.schedules/o2m-graph"
	_description = "SRM Contract Delivery Schedules"

class ViewModelO2MMdxSrmContractItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.contract.item.delivery.schedules"
	_view_name = "srm.contract.item.delivery.schedules/o2m-mdx"
	_description = "SRM Contract Delivery Schedules"

class ViewModelO2MListSrmContractItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.item.delivery.schedules"
	_view_name = "srm.contract.item.delivery.schedules/o2m-list"
	_description = "SRM Contract Delivery Schedules"
