from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseOrderCategories(ViewModelSearchController):
	_name = "search:purchase.order.categories"
	_view_name = "purchase.order.categories/search"
	_description = "Categories Purchase Order"

class ViewModelFindPurchaseOrderCategories(ViewModelFindController):
	_name = "find:purchase.order.categories"
	_view_name = "purchase.order.categories/find"
	_description = "Categories Purchase Order"

class ViewModelListPurchaseOrderCategories(ViewModelListController):
	_name = "list:purchase.order.categories"
	_view_name = "purchase.order.categories/list"
	_description = "Categories Purchase Order"

class ViewModelFormModalPurchaseOrderCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.order.categories"
	_view_name = "purchase.order.categories/form.modal"
	_description = "Categories Purchase Order"

class ViewModelFormPurchaseOrderCategories(ViewModelFormController):
	_name = "form:purchase.order.categories"
	_view_name = "purchase.order.categories/form"
	_description = "Categories Purchase Order"

class ViewModelTreePurchaseOrderCategories(ViewModelTreeController):
	_name = "tree:purchase.order.categories"
	_view_name = "purchase.order.categories/tree"
	_description = "Categories Purchase Order"
