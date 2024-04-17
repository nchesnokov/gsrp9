from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseUnitCategories(ViewModelSearchController):
	_name = "search:purchase.unit.categories"
	_view_name = "purchase.unit.categories/search"
	_description = "Categories Purchase Unit"

class ViewModelFindPurchaseUnitCategories(ViewModelFindController):
	_name = "find:purchase.unit.categories"
	_view_name = "purchase.unit.categories/find"
	_description = "Categories Purchase Unit"

class ViewModelListPurchaseUnitCategories(ViewModelListController):
	_name = "list:purchase.unit.categories"
	_view_name = "purchase.unit.categories/list"
	_description = "Categories Purchase Unit"

class ViewModelFormModalPurchaseUnitCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.unit.categories"
	_view_name = "purchase.unit.categories/form.modal"
	_description = "Categories Purchase Unit"

class ViewModelFormPurchaseUnitCategories(ViewModelFormController):
	_name = "form:purchase.unit.categories"
	_view_name = "purchase.unit.categories/form"
	_description = "Categories Purchase Unit"

class ViewModelTreePurchaseUnitCategories(ViewModelTreeController):
	_name = "tree:purchase.unit.categories"
	_view_name = "purchase.unit.categories/tree"
	_description = "Categories Purchase Unit"
