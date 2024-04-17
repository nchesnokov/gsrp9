from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderItemDeliverySchedules(ViewModelFindController):
	_name = "find:purchase.order.item.delivery.schedules"
	_view_name = "purchase.order.item.delivery.schedules/find"
	_description = "Purchase Order Item Delivery Schedules"

class ViewModelO2MFormPurchaseOrderItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.item.delivery.schedules"
	_view_name = "purchase.order.item.delivery.schedules/o2m-form"
	_description = "Purchase Order Item Delivery Schedules"

class ViewModelO2MListPurchaseOrderItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.item.delivery.schedules"
	_view_name = "purchase.order.item.delivery.schedules/o2m-list"
	_description = "Purchase Order Item Delivery Schedules"
