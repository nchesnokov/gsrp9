from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmSegmentCategories(ViewModelSearchController):
	_name = "search:crm.segment.categories"
	_view_name = "crm.segment.categories/search"
	_description = "Categories CRM Segment"

class ViewModelFindCrmSegmentCategories(ViewModelFindController):
	_name = "find:crm.segment.categories"
	_view_name = "crm.segment.categories/find"
	_description = "Categories CRM Segment"

class ViewModelListCrmSegmentCategories(ViewModelListController):
	_name = "list:crm.segment.categories"
	_view_name = "crm.segment.categories/list"
	_description = "Categories CRM Segment"

class ViewModelFormModalCrmSegmentCategories(ViewModelFormModalController):
	_name = "form.modal:crm.segment.categories"
	_view_name = "crm.segment.categories/form.modal"
	_description = "Categories CRM Segment"

class ViewModelFormCrmSegmentCategories(ViewModelFormController):
	_name = "form:crm.segment.categories"
	_view_name = "crm.segment.categories/form"
	_description = "Categories CRM Segment"

class ViewModelTreeCrmSegmentCategories(ViewModelTreeController):
	_name = "tree:crm.segment.categories"
	_view_name = "crm.segment.categories/tree"
	_description = "Categories CRM Segment"
