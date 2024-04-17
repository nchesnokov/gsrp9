from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleOrderCategories(ViewModelSearchController):
	_name = "search:sale.order.categories"
	_view_name = "sale.order.categories/search"
	_description = "Category Sale Order"

class ViewModelFindSaleOrderCategories(ViewModelFindController):
	_name = "find:sale.order.categories"
	_view_name = "sale.order.categories/find"
	_description = "Category Sale Order"

class ViewModelListSaleOrderCategories(ViewModelListController):
	_name = "list:sale.order.categories"
	_view_name = "sale.order.categories/list"
	_description = "Category Sale Order"

class ViewModelFormModalSaleOrderCategories(ViewModelFormModalController):
	_name = "form.modal:sale.order.categories"
	_view_name = "sale.order.categories/form.modal"
	_description = "Category Sale Order"

class ViewModelFormSaleOrderCategories(ViewModelFormController):
	_name = "form:sale.order.categories"
	_view_name = "sale.order.categories/form"
	_description = "Category Sale Order"

class ViewModelTreeSaleOrderCategories(ViewModelTreeController):
	_name = "tree:sale.order.categories"
	_view_name = "sale.order.categories/tree"
	_description = "Category Sale Order"
