from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseSubdivisionCategories(ViewModelSearchController):
	_name = "search:purchase.subdivision.categories"
	_view_name = "purchase.subdivision.categories/search"
	_description = "Categories Purchase Subdivision"

class ViewModelFindPurchaseSubdivisionCategories(ViewModelFindController):
	_name = "find:purchase.subdivision.categories"
	_view_name = "purchase.subdivision.categories/find"
	_description = "Categories Purchase Subdivision"

class ViewModelListPurchaseSubdivisionCategories(ViewModelListController):
	_name = "list:purchase.subdivision.categories"
	_view_name = "purchase.subdivision.categories/list"
	_description = "Categories Purchase Subdivision"

class ViewModelFormModalPurchaseSubdivisionCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.subdivision.categories"
	_view_name = "purchase.subdivision.categories/form.modal"
	_description = "Categories Purchase Subdivision"

class ViewModelFormPurchaseSubdivisionCategories(ViewModelFormController):
	_name = "form:purchase.subdivision.categories"
	_view_name = "purchase.subdivision.categories/form"
	_description = "Categories Purchase Subdivision"

class ViewModelTreePurchaseSubdivisionCategories(ViewModelTreeController):
	_name = "tree:purchase.subdivision.categories"
	_view_name = "purchase.subdivision.categories/tree"
	_description = "Categories Purchase Subdivision"
