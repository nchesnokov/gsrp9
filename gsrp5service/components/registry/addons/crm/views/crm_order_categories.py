from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmOrderCategories(ViewModelSearch):
	_name = "model.search.crm.order.categories"
	_model = "crm.order.categories"
	_description = "Category CRM Order"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelFindCrmOrderCategories(ViewModelFind):
	_name = "model.find.crm.order.categories"
	_model = "crm.order.categories"
	_description = "Category CRM Order"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MFormCrmOrderCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.categories"
	_model = "crm.order.categories"
	_description = "Category CRM Order"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'orders', 'note']

class ViewModelTreeCrmOrderCategories(ViewModelTree):
	_name = "model.tree.crm.order.categories"
	_model = "crm.order.categories"
	_description = "Category CRM Order"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MTreeCrmOrderCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.order.categories"
	_model = "crm.order.categories"
	_description = "Category CRM Order"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MListCrmOrderCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.categories"
	_model = "crm.order.categories"
	_description = "Category CRM Order"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'orders']
