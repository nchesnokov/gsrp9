from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmInvoiceTypes(ViewModelSearch):
	_name = "model.search.crm.invoice.types"
	_model = "crm.invoice.types"
	_description = "Types CRM Invoice"
	_columns = ['name', 'htschema', 'itschema']

class ViewModelFindCrmInvoiceTypes(ViewModelFind):
	_name = "model.find.crm.invoice.types"
	_model = "crm.invoice.types"
	_description = "Types CRM Invoice"
	_columns = ['name', 'htschema', 'itschema']

class ViewModelO2MFormCrmInvoiceTypes(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.types"
	_model = "crm.invoice.types"
	_description = "Types CRM Invoice"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'note']

class ViewModelO2MListCrmInvoiceTypes(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.types"
	_model = "crm.invoice.types"
	_description = "Types CRM Invoice"
	_columns = ['name', 'htschema', 'itschema', 'roles']
