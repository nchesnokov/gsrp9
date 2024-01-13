from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestItems(ViewModelFind):
	_name = "model.find.crm.request.items"
	_model = "crm.request.items"
	_description = "CRM Request Items"
	_columns = ['request_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom', 'note']

class ViewModelO2MFormCrmRequestItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.items"
	_model = "crm.request.items"
	_description = "CRM Request Items"
	_columns = ['request_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom', 'delivery_schedules', 'pricing', 'roles', 'texts', 'plates', 'payments', 'note']

class ViewModelO2MListCrmRequestItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.items"
	_model = "crm.request.items"
	_description = "CRM Request Items"
	_columns = ['request_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom', 'delivery_schedules', 'pricing', 'roles', 'texts', 'plates', 'payments', 'note']
