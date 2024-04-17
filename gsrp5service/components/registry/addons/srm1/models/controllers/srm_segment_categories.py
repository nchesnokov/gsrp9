from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmSegmentCategories(ViewModelSearchController):
	_name = "search:srm.segment.categories"
	_view_name = "srm.segment.categories/search"
	_description = "Categories SRM Segment"

class ViewModelFindSrmSegmentCategories(ViewModelFindController):
	_name = "find:srm.segment.categories"
	_view_name = "srm.segment.categories/find"
	_description = "Categories SRM Segment"

class ViewModelListSrmSegmentCategories(ViewModelListController):
	_name = "list:srm.segment.categories"
	_view_name = "srm.segment.categories/list"
	_description = "Categories SRM Segment"

class ViewModelFormModalSrmSegmentCategories(ViewModelFormModalController):
	_name = "form.modal:srm.segment.categories"
	_view_name = "srm.segment.categories/form.modal"
	_description = "Categories SRM Segment"

class ViewModelFormSrmSegmentCategories(ViewModelFormController):
	_name = "form:srm.segment.categories"
	_view_name = "srm.segment.categories/form"
	_description = "Categories SRM Segment"

class ViewModelTreeSrmSegmentCategories(ViewModelTreeController):
	_name = "tree:srm.segment.categories"
	_view_name = "srm.segment.categories/tree"
	_description = "Categories SRM Segment"
