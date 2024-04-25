from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseSegmentCategories(ViewModelSearchController):
	_name = "search:purchase.segment.categories"
	_view_name = "purchase.segment.categories/search"
	_description = "Categories Purchase Segment"

class ViewModelFindPurchaseSegmentCategories(ViewModelFindController):
	_name = "find:purchase.segment.categories"
	_view_name = "purchase.segment.categories/find"
	_description = "Categories Purchase Segment"

class ViewModelListPurchaseSegmentCategories(ViewModelListController):
	_name = "list:purchase.segment.categories"
	_view_name = "purchase.segment.categories/list"
	_description = "Categories Purchase Segment"

class ViewModelFormModalPurchaseSegmentCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.segment.categories"
	_view_name = "purchase.segment.categories/form.modal"
	_description = "Categories Purchase Segment"

class ViewModelFormPurchaseSegmentCategories(ViewModelFormController):
	_name = "form:purchase.segment.categories"
	_view_name = "purchase.segment.categories/form"
	_description = "Categories Purchase Segment"

class ViewModelTreePurchaseSegmentCategories(ViewModelTreeController):
	_name = "tree:purchase.segment.categories"
	_view_name = "purchase.segment.categories/tree"
	_description = "Categories Purchase Segment"
