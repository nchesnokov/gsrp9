from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOfferItemDeliverySchedules(ViewModelFind):
	_name = "model.find.crm.offer.item.delivery.schedules"
	_model = "crm.offer.item.delivery.schedules"
	_description = "CRM Offer Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']

class ViewModelO2MFormCrmOfferItemDeliverySchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.offer.item.delivery.schedules"
	_model = "crm.offer.item.delivery.schedules"
	_description = "CRM Offer Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']

class ViewModelO2MListCrmOfferItemDeliverySchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.offer.item.delivery.schedules"
	_model = "crm.offer.item.delivery.schedules"
	_description = "CRM Offer Item Delivery Schedules"
	_columns = ['item_id', 'quantity', 'schedule', 'note']
