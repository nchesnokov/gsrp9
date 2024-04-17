from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderItemDeliverySchedules(ViewModelFindController):
	_name = "find:sale.order.item.delivery.schedules"
	_view_name = "sale.order.item.delivery.schedules/find"
	_description = "Sales Order Item Delivery Schedules"

class ViewModelO2MFormSaleOrderItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.item.delivery.schedules"
	_view_name = "sale.order.item.delivery.schedules/o2m-form"
	_description = "Sales Order Item Delivery Schedules"

class ViewModelO2MListSaleOrderItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:sale.order.item.delivery.schedules"
	_view_name = "sale.order.item.delivery.schedules/o2m-list"
	_description = "Sales Order Item Delivery Schedules"
