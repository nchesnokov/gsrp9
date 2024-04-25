from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractItemDeliverySchedules(ViewModelFindController):
	_name = "find:crm.contract.item.delivery.schedules"
	_view_name = "crm.contract.item.delivery.schedules/find"
	_description = "Crm Contract Item Delivery Schedules"

class ViewModelO2MFormCrmContractItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.item.delivery.schedules"
	_view_name = "crm.contract.item.delivery.schedules/o2m-form"
	_description = "Crm Contract Item Delivery Schedules"

class ViewModelO2MListCrmContractItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.item.delivery.schedules"
	_view_name = "crm.contract.item.delivery.schedules/o2m-list"
	_description = "Crm Contract Item Delivery Schedules"
