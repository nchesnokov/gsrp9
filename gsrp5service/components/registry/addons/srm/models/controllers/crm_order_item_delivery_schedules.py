from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderItemDeliverySchedules(ViewModelFindController):
	_name = "find:crm.order.item.delivery.schedules"
	_view_name = "crm.order.item.delivery.schedules/find"
	_description = "CRMs Order Item Delivery Schedules"

class ViewModelO2MFormCrmOrderItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.item.delivery.schedules"
	_view_name = "crm.order.item.delivery.schedules/o2m-form"
	_description = "CRMs Order Item Delivery Schedules"

class ViewModelO2MListCrmOrderItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.order.item.delivery.schedules"
	_view_name = "crm.order.item.delivery.schedules/o2m-list"
	_description = "CRMs Order Item Delivery Schedules"
