from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmRequestCategories(ViewModelSearch):
	_name = "model.search.crm.request.categories"
	_model = "crm.request.categories"
	_description = "Category CRM Request"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmRequestCategories(ViewModelFind):
	_name = "model.find.crm.request.categories"
	_model = "crm.request.categories"
	_description = "Category CRM Request"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmRequestCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.categories"
	_model = "crm.request.categories"
	_description = "Category CRM Request"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'requests', 'note']

class ViewModelTreeCrmRequestCategories(ViewModelTree):
	_name = "model.tree.crm.request.categories"
	_model = "crm.request.categories"
	_description = "Category CRM Request"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmRequestCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.request.categories"
	_model = "crm.request.categories"
	_description = "Category CRM Request"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmRequestCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.categories"
	_model = "crm.request.categories"
	_description = "Category CRM Request"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'requests', 'note']
