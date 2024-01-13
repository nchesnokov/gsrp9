from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmUnitCategories(ViewModelSearch):
	_name = "model.search.crm.unit.categories"
	_model = "crm.unit.categories"
	_description = "Categories CRM Unit"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmUnitCategories(ViewModelFind):
	_name = "model.find.crm.unit.categories"
	_model = "crm.unit.categories"
	_description = "Categories CRM Unit"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmUnitCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.unit.categories"
	_model = "crm.unit.categories"
	_description = "Categories CRM Unit"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'units', 'note']

class ViewModelTreeCrmUnitCategories(ViewModelTree):
	_name = "model.tree.crm.unit.categories"
	_model = "crm.unit.categories"
	_description = "Categories CRM Unit"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmUnitCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.unit.categories"
	_model = "crm.unit.categories"
	_description = "Categories CRM Unit"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmUnitCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.unit.categories"
	_model = "crm.unit.categories"
	_description = "Categories CRM Unit"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'units', 'note']
