from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractItemDeliverySchedules(ViewModelFind):
	_name = "model.find.crm.contract.item.delivery.schedules"
	_model = "crm.contract.item.delivery.schedules"
	_description = "Crm Contract Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule']

class ViewModelO2MFormCrmContractItemDeliverySchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.item.delivery.schedules"
	_model = "crm.contract.item.delivery.schedules"
	_description = "Crm Contract Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']

class ViewModelO2MListCrmContractItemDeliverySchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.item.delivery.schedules"
	_model = "crm.contract.item.delivery.schedules"
	_description = "Crm Contract Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule']
