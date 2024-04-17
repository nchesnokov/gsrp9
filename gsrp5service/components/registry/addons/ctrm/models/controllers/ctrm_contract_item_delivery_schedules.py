from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmContractItemDeliverySchedules(ViewModelFindController):
	_name = "find:ctrm.contract.item.delivery.schedules"
	_view_name = "ctrm.contract.item.delivery.schedules/find"
	_description = "CTRM Contract Item Delivery Schedules"

class ViewModelO2MFormCtrmContractItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.contract.item.delivery.schedules"
	_view_name = "ctrm.contract.item.delivery.schedules/o2m-form"
	_description = "CTRM Contract Item Delivery Schedules"

class ViewModelO2MListCtrmContractItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:ctrm.contract.item.delivery.schedules"
	_view_name = "ctrm.contract.item.delivery.schedules/o2m-list"
	_description = "CTRM Contract Item Delivery Schedules"
