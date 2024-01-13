from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmInvoiceTexts(ViewModelFind):
	_name = "model.find.crm.invoice.texts"
	_model = "crm.invoice.texts"
	_description = "CRM Invoce Texts"
	_columns = ['invoice_id', 'seq', 'text_id', 'descr']

class ViewModelO2MFormCrmInvoiceTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.texts"
	_model = "crm.invoice.texts"
	_description = "CRM Invoce Texts"
	_columns = ['invoice_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmInvoiceTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.texts"
	_model = "crm.invoice.texts"
	_description = "CRM Invoce Texts"
	_columns = ['invoice_id', 'seq', 'text_id', 'descr']
