from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmSegmentCategories(ViewModelSearch):
	_name = "model.search.crm.segment.categories"
	_model = "crm.segment.categories"
	_description = "Categories CRM Segment"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelFindCrmSegmentCategories(ViewModelFind):
	_name = "model.find.crm.segment.categories"
	_model = "crm.segment.categories"
	_description = "Categories CRM Segment"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MFormCrmSegmentCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.segment.categories"
	_model = "crm.segment.categories"
	_description = "Categories CRM Segment"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'segments', 'note']

class ViewModelTreeCrmSegmentCategories(ViewModelTree):
	_name = "model.tree.crm.segment.categories"
	_model = "crm.segment.categories"
	_description = "Categories CRM Segment"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MTreeCrmSegmentCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.segment.categories"
	_model = "crm.segment.categories"
	_description = "Categories CRM Segment"
	_columns = ['name', 'parent_id', 'fullname', 'note']

class ViewModelO2MListCrmSegmentCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.segment.categories"
	_model = "crm.segment.categories"
	_description = "Categories CRM Segment"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'segments', 'note']
