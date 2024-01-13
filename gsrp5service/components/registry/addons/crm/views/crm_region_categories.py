from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmRegionCategories(ViewModelSearch):
	_name = "model.search.crm.region.categories"
	_model = "crm.region.categories"
	_description = "Categories CRM Region"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmRegionCategories(ViewModelFind):
	_name = "model.find.crm.region.categories"
	_model = "crm.region.categories"
	_description = "Categories CRM Region"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmRegionCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.region.categories"
	_model = "crm.region.categories"
	_description = "Categories CRM Region"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'segments', 'note']

class ViewModelTreeCrmRegionCategories(ViewModelTree):
	_name = "model.tree.crm.region.categories"
	_model = "crm.region.categories"
	_description = "Categories CRM Region"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmRegionCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.region.categories"
	_model = "crm.region.categories"
	_description = "Categories CRM Region"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmRegionCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.region.categories"
	_model = "crm.region.categories"
	_description = "Categories CRM Region"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'segments', 'note']
