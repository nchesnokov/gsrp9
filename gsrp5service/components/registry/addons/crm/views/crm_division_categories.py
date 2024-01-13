from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmDivisionCategories(ViewModelSearch):
	_name = "model.search.crm.division.categories"
	_model = "crm.division.categories"
	_description = "Categories CRM Division"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmDivisionCategories(ViewModelFind):
	_name = "model.find.crm.division.categories"
	_model = "crm.division.categories"
	_description = "Categories CRM Division"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmDivisionCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.division.categories"
	_model = "crm.division.categories"
	_description = "Categories CRM Division"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'divisions', 'note']

class ViewModelTreeCrmDivisionCategories(ViewModelTree):
	_name = "model.tree.crm.division.categories"
	_model = "crm.division.categories"
	_description = "Categories CRM Division"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmDivisionCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.division.categories"
	_model = "crm.division.categories"
	_description = "Categories CRM Division"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmDivisionCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.division.categories"
	_model = "crm.division.categories"
	_description = "Categories CRM Division"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'divisions', 'note']
