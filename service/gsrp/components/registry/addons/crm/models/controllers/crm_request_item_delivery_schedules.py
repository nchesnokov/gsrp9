from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestItemDeliverySchedules(ViewModelFindController):
	_name = "find:crm.request.item.delivery.schedules"
	_view_name = "crm.request.item.delivery.schedules/find"
	_description = "CRM Request Item Delivery Schedules"

class ViewModelO2MFormCrmRequestItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.item.delivery.schedules"
	_view_name = "crm.request.item.delivery.schedules/o2m-form"
	_description = "CRM Request Item Delivery Schedules"

class ViewModelO2MListCrmRequestItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.request.item.delivery.schedules"
	_view_name = "crm.request.item.delivery.schedules/o2m-list"
	_description = "CRM Request Item Delivery Schedules"
