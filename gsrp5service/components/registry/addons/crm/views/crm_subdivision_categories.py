from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmSubdivisionCategories(ViewModelSearch):
	_name = "model.search.crm.subdivision.categories"
	_model = "crm.subdivision.categories"
	_description = "Categories CRM Subdivision"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmSubdivisionCategories(ViewModelFind):
	_name = "model.find.crm.subdivision.categories"
	_model = "crm.subdivision.categories"
	_description = "Categories CRM Subdivision"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmSubdivisionCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.subdivision.categories"
	_model = "crm.subdivision.categories"
	_description = "Categories CRM Subdivision"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'subdivisions', 'note']

class ViewModelTreeCrmSubdivisionCategories(ViewModelTree):
	_name = "model.tree.crm.subdivision.categories"
	_model = "crm.subdivision.categories"
	_description = "Categories CRM Subdivision"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmSubdivisionCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.subdivision.categories"
	_model = "crm.subdivision.categories"
	_description = "Categories CRM Subdivision"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmSubdivisionCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.subdivision.categories"
	_model = "crm.subdivision.categories"
	_description = "Categories CRM Subdivision"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'subdivisions', 'note']
