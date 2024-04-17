from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseAreaCategories(ViewModelSearchController):
	_name = "search:purchase.area.categories"
	_view_name = "purchase.area.categories/search"
	_description = "Categories Purchase Area"

class ViewModelFindPurchaseAreaCategories(ViewModelFindController):
	_name = "find:purchase.area.categories"
	_view_name = "purchase.area.categories/find"
	_description = "Categories Purchase Area"

class ViewModelListPurchaseAreaCategories(ViewModelListController):
	_name = "list:purchase.area.categories"
	_view_name = "purchase.area.categories/list"
	_description = "Categories Purchase Area"

class ViewModelFormModalPurchaseAreaCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.area.categories"
	_view_name = "purchase.area.categories/form.modal"
	_description = "Categories Purchase Area"

class ViewModelFormPurchaseAreaCategories(ViewModelFormController):
	_name = "form:purchase.area.categories"
	_view_name = "purchase.area.categories/form"
	_description = "Categories Purchase Area"

class ViewModelTreePurchaseAreaCategories(ViewModelTreeController):
	_name = "tree:purchase.area.categories"
	_view_name = "purchase.area.categories/tree"
	_description = "Categories Purchase Area"
