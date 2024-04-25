from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleInvoiceItemDeliverySchedules(ViewModelFindController):
	_name = "find:sale.invoice.item.delivery.schedules"
	_view_name = "sale.invoice.item.delivery.schedules/find"
	_description = "Sales Order Item Delivery Schedules"

class ViewModelO2MFormSaleInvoiceItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:sale.invoice.item.delivery.schedules"
	_view_name = "sale.invoice.item.delivery.schedules/o2m-form"
	_description = "Sales Order Item Delivery Schedules"

class ViewModelO2MListSaleInvoiceItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:sale.invoice.item.delivery.schedules"
	_view_name = "sale.invoice.item.delivery.schedules/o2m-list"
	_description = "Sales Order Item Delivery Schedules"
