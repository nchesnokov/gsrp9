from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOfferItems(ViewModelFind):
	_name = "model.find.crm.offer.items"
	_model = "crm.offer.items"
	_description = "CRM Offer Items"
	_columns = ['offer_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MFormCrmOfferItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.offer.items"
	_model = "crm.offer.items"
	_description = "CRM Offer Items"
	_columns = ['offer_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'delivery_schedules', 'roles', 'texts', 'note']

class ViewModelO2MListCrmOfferItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.offer.items"
	_model = "crm.offer.items"
	_description = "CRM Offer Items"
	_columns = ['offer_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'delivery_schedules', 'roles', 'texts', 'note']
