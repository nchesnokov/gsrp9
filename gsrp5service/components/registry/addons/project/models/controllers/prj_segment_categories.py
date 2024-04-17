from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjSegmentCategories(ViewModelSearchController):
	_name = "search:prj.segment.categories"
	_view_name = "prj.segment.categories/search"
	_description = "Categories Project Segment"

class ViewModelFindPrjSegmentCategories(ViewModelFindController):
	_name = "find:prj.segment.categories"
	_view_name = "prj.segment.categories/find"
	_description = "Categories Project Segment"

class ViewModelListPrjSegmentCategories(ViewModelListController):
	_name = "list:prj.segment.categories"
	_view_name = "prj.segment.categories/list"
	_description = "Categories Project Segment"

class ViewModelFormModalPrjSegmentCategories(ViewModelFormModalController):
	_name = "form.modal:prj.segment.categories"
	_view_name = "prj.segment.categories/form.modal"
	_description = "Categories Project Segment"

class ViewModelFormPrjSegmentCategories(ViewModelFormController):
	_name = "form:prj.segment.categories"
	_view_name = "prj.segment.categories/form"
	_description = "Categories Project Segment"

class ViewModelTreePrjSegmentCategories(ViewModelTreeController):
	_name = "tree:prj.segment.categories"
	_view_name = "prj.segment.categories/tree"
	_description = "Categories Project Segment"
