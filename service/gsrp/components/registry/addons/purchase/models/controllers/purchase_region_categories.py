from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseRegionCategories(ViewModelSearchController):
	_name = "search:purchase.region.categories"
	_view_name = "purchase.region.categories/search"
	_description = "Categories Purchase Region"

class ViewModelFindPurchaseRegionCategories(ViewModelFindController):
	_name = "find:purchase.region.categories"
	_view_name = "purchase.region.categories/find"
	_description = "Categories Purchase Region"

class ViewModelListPurchaseRegionCategories(ViewModelListController):
	_name = "list:purchase.region.categories"
	_view_name = "purchase.region.categories/list"
	_description = "Categories Purchase Region"

class ViewModelFormModalPurchaseRegionCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.region.categories"
	_view_name = "purchase.region.categories/form.modal"
	_description = "Categories Purchase Region"

class ViewModelFormPurchaseRegionCategories(ViewModelFormController):
	_name = "form:purchase.region.categories"
	_view_name = "purchase.region.categories/form"
	_description = "Categories Purchase Region"

class ViewModelTreePurchaseRegionCategories(ViewModelTreeController):
	_name = "tree:purchase.region.categories"
	_view_name = "purchase.region.categories/tree"
	_description = "Categories Purchase Region"
