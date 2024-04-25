from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleSegmentCategories(ViewModelSearchController):
	_name = "search:sale.segment.categories"
	_view_name = "sale.segment.categories/search"
	_description = "Categories Sale Segment"

class ViewModelFindSaleSegmentCategories(ViewModelFindController):
	_name = "find:sale.segment.categories"
	_view_name = "sale.segment.categories/find"
	_description = "Categories Sale Segment"

class ViewModelListSaleSegmentCategories(ViewModelListController):
	_name = "list:sale.segment.categories"
	_view_name = "sale.segment.categories/list"
	_description = "Categories Sale Segment"

class ViewModelFormModalSaleSegmentCategories(ViewModelFormModalController):
	_name = "form.modal:sale.segment.categories"
	_view_name = "sale.segment.categories/form.modal"
	_description = "Categories Sale Segment"

class ViewModelFormSaleSegmentCategories(ViewModelFormController):
	_name = "form:sale.segment.categories"
	_view_name = "sale.segment.categories/form"
	_description = "Categories Sale Segment"

class ViewModelTreeSaleSegmentCategories(ViewModelTreeController):
	_name = "tree:sale.segment.categories"
	_view_name = "sale.segment.categories/tree"
	_description = "Categories Sale Segment"
