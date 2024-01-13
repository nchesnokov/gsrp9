from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmInvoiceItemTexts(ViewModelFind):
	_name = "model.find.crm.invoice.item.texts"
	_model = "crm.invoice.item.texts"
	_description = "CRM Invoce Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelO2MFormCrmInvoiceItemTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.item.texts"
	_model = "crm.invoice.item.texts"
	_description = "CRM Invoce Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmInvoiceItemTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.item.texts"
	_model = "crm.invoice.item.texts"
	_description = "CRM Invoce Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']
