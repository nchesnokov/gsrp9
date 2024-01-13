from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmAreaCategories(ViewModelSearch):
	_name = "model.search.crm.area.categories"
	_model = "crm.area.categories"
	_description = "Categories CRM Area"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmAreaCategories(ViewModelFind):
	_name = "model.find.crm.area.categories"
	_model = "crm.area.categories"
	_description = "Categories CRM Area"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmAreaCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.area.categories"
	_model = "crm.area.categories"
	_description = "Categories CRM Area"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'areas', 'note']

class ViewModelTreeCrmAreaCategories(ViewModelTree):
	_name = "model.tree.crm.area.categories"
	_model = "crm.area.categories"
	_description = "Categories CRM Area"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmAreaCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.area.categories"
	_model = "crm.area.categories"
	_description = "Categories CRM Area"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmAreaCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.area.categories"
	_model = "crm.area.categories"
	_description = "Categories CRM Area"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'areas', 'note']
