from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmInvoiceItemDeliverySchedules(ViewModelFindController):
	_name = "find:crm.invoice.item.delivery.schedules"
	_view_name = "crm.invoice.item.delivery.schedules/find"
	_description = "CRMs Order Item Delivery Schedules"

class ViewModelO2MFormCrmInvoiceItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.invoice.item.delivery.schedules"
	_view_name = "crm.invoice.item.delivery.schedules/o2m-form"
	_description = "CRMs Order Item Delivery Schedules"

class ViewModelO2MListCrmInvoiceItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.invoice.item.delivery.schedules"
	_view_name = "crm.invoice.item.delivery.schedules/o2m-list"
	_description = "CRMs Order Item Delivery Schedules"
