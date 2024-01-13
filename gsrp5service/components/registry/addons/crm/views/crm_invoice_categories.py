from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmInvoiceCategories(ViewModelSearch):
	_name = "model.search.crm.invoice.categories"
	_model = "crm.invoice.categories"
	_description = "Category CRM Invoice"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelFindCrmInvoiceCategories(ViewModelFind):
	_name = "model.find.crm.invoice.categories"
	_model = "crm.invoice.categories"
	_description = "Category CRM Invoice"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MFormCrmInvoiceCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.categories"
	_model = "crm.invoice.categories"
	_description = "Category CRM Invoice"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'invoices', 'note']

class ViewModelTreeCrmInvoiceCategories(ViewModelTree):
	_name = "model.tree.crm.invoice.categories"
	_model = "crm.invoice.categories"
	_description = "Category CRM Invoice"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MTreeCrmInvoiceCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.invoice.categories"
	_model = "crm.invoice.categories"
	_description = "Category CRM Invoice"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MListCrmInvoiceCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.categories"
	_model = "crm.invoice.categories"
	_description = "Category CRM Invoice"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'invoices']
