from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseInvoceCategories(ViewModelSearchController):
	_name = "search:purchase.invoce.categories"
	_view_name = "purchase.invoce.categories/search"
	_description = "Categories Purchase Invoce"

class ViewModelFindPurchaseInvoceCategories(ViewModelFindController):
	_name = "find:purchase.invoce.categories"
	_view_name = "purchase.invoce.categories/find"
	_description = "Categories Purchase Invoce"

class ViewModelListPurchaseInvoceCategories(ViewModelListController):
	_name = "list:purchase.invoce.categories"
	_view_name = "purchase.invoce.categories/list"
	_description = "Categories Purchase Invoce"

class ViewModelFormModalPurchaseInvoceCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.invoce.categories"
	_view_name = "purchase.invoce.categories/form.modal"
	_description = "Categories Purchase Invoce"

class ViewModelFormPurchaseInvoceCategories(ViewModelFormController):
	_name = "form:purchase.invoce.categories"
	_view_name = "purchase.invoce.categories/form"
	_description = "Categories Purchase Invoce"

class ViewModelTreePurchaseInvoceCategories(ViewModelTreeController):
	_name = "tree:purchase.invoce.categories"
	_view_name = "purchase.invoce.categories/tree"
	_description = "Categories Purchase Invoce"
