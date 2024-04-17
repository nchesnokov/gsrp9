from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseDivisionCategories(ViewModelSearchController):
	_name = "search:purchase.division.categories"
	_view_name = "purchase.division.categories/search"
	_description = "Categories Purchase Division"

class ViewModelFindPurchaseDivisionCategories(ViewModelFindController):
	_name = "find:purchase.division.categories"
	_view_name = "purchase.division.categories/find"
	_description = "Categories Purchase Division"

class ViewModelListPurchaseDivisionCategories(ViewModelListController):
	_name = "list:purchase.division.categories"
	_view_name = "purchase.division.categories/list"
	_description = "Categories Purchase Division"

class ViewModelFormModalPurchaseDivisionCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.division.categories"
	_view_name = "purchase.division.categories/form.modal"
	_description = "Categories Purchase Division"

class ViewModelFormPurchaseDivisionCategories(ViewModelFormController):
	_name = "form:purchase.division.categories"
	_view_name = "purchase.division.categories/form"
	_description = "Categories Purchase Division"

class ViewModelTreePurchaseDivisionCategories(ViewModelTreeController):
	_name = "tree:purchase.division.categories"
	_view_name = "purchase.division.categories/tree"
	_description = "Categories Purchase Division"
