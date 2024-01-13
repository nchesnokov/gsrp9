from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderItemDeliverySchedules(ViewModelFind):
	_name = "model.find.crm.order.item.delivery.schedules"
	_model = "crm.order.item.delivery.schedules"
	_description = "CRMs Order Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule']

class ViewModelO2MFormCrmOrderItemDeliverySchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.item.delivery.schedules"
	_model = "crm.order.item.delivery.schedules"
	_description = "CRMs Order Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']

class ViewModelO2MListCrmOrderItemDeliverySchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.item.delivery.schedules"
	_model = "crm.order.item.delivery.schedules"
	_description = "CRMs Order Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule']
