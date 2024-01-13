from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmInvoiceItems(ViewModelFind):
	_name = "model.find.crm.invoice.items"
	_model = "crm.invoice.items"
	_description = "CRMs Invoice Items"
	_columns = ['invoice_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount']

class ViewModelO2MFormCrmInvoiceItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.items"
	_model = "crm.invoice.items"
	_description = "CRMs Invoice Items"
	_columns = ['invoice_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'delivery_schedules', 'roles', 'texts', 'note']

class ViewModelO2MListCrmInvoiceItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.items"
	_model = "crm.invoice.items"
	_description = "CRMs Invoice Items"
	_columns = ['invoice_id', 'product', 'quantity', 'uom', 'price', 'currency', 'unit', 'uop', 'amount', 'vat_code', 'vat_amount', 'total_amount', 'delivery_schedules', 'roles', 'texts']
