from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmInvoiceItemDeliverySchedules(ViewModelFind):
	_name = "model.find.crm.invoice.item.delivery.schedules"
	_model = "crm.invoice.item.delivery.schedules"
	_description = "CRMs Order Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule']

class ViewModelO2MFormCrmInvoiceItemDeliverySchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.item.delivery.schedules"
	_model = "crm.invoice.item.delivery.schedules"
	_description = "CRMs Order Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']

class ViewModelO2MListCrmInvoiceItemDeliverySchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.item.delivery.schedules"
	_model = "crm.invoice.item.delivery.schedules"
	_description = "CRMs Order Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule']
