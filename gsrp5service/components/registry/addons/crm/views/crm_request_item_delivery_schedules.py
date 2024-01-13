from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestItemDeliverySchedules(ViewModelFind):
	_name = "model.find.crm.request.item.delivery.schedules"
	_model = "crm.request.item.delivery.schedules"
	_description = "CRM Request Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']

class ViewModelO2MFormCrmRequestItemDeliverySchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.item.delivery.schedules"
	_model = "crm.request.item.delivery.schedules"
	_description = "CRM Request Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']

class ViewModelO2MListCrmRequestItemDeliverySchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.item.delivery.schedules"
	_model = "crm.request.item.delivery.schedules"
	_description = "CRM Request Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']
