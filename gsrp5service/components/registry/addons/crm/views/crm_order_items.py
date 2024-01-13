from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderItems(ViewModelFind):
	_name = "model.find.crm.order.items"
	_model = "crm.order.items"
	_description = "CRM Order Items"
	_columns = ['order_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom']

class ViewModelO2MFormCrmOrderItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.items"
	_model = "crm.order.items"
	_description = "CRM Order Items"
	_columns = ['order_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom', 'delivery_schedules', 'pricing', 'roles', 'texts', 'plates', 'payments', 'note']

class ViewModelO2MListCrmOrderItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.items"
	_model = "crm.order.items"
	_description = "CRM Order Items"
	_columns = ['order_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom', 'delivery_schedules', 'pricing', 'roles', 'texts', 'plates', 'payments']
