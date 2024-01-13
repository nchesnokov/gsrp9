from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractItems(ViewModelFind):
	_name = "model.find.crm.contract.items"
	_model = "crm.contract.items"
	_description = "Crm Contract Items"
	_columns = ['contract_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom']

class ViewModelO2MFormCrmContractItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.items"
	_model = "crm.contract.items"
	_description = "Crm Contract Items"
	_columns = ['contract_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom', 'delivery_schedules', 'pricing', 'roles', 'texts', 'plates', 'payments', 'note']

class ViewModelO2MListCrmContractItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.items"
	_model = "crm.contract.items"
	_description = "Crm Contract Items"
	_columns = ['contract_id', 'itype_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'volume', 'volume_total', 'volume_uom', 'weight', 'weight_total', 'weight_uom', 'delivery_schedules', 'pricing', 'roles', 'texts', 'plates', 'payments']
