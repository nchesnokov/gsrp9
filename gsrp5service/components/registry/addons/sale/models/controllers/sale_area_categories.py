from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleAreaCategories(ViewModelSearchController):
	_name = "search:sale.area.categories"
	_view_name = "sale.area.categories/search"
	_description = "Categories Sale Area"

class ViewModelFindSaleAreaCategories(ViewModelFindController):
	_name = "find:sale.area.categories"
	_view_name = "sale.area.categories/find"
	_description = "Categories Sale Area"

class ViewModelListSaleAreaCategories(ViewModelListController):
	_name = "list:sale.area.categories"
	_view_name = "sale.area.categories/list"
	_description = "Categories Sale Area"

class ViewModelFormModalSaleAreaCategories(ViewModelFormModalController):
	_name = "form.modal:sale.area.categories"
	_view_name = "sale.area.categories/form.modal"
	_description = "Categories Sale Area"

class ViewModelFormSaleAreaCategories(ViewModelFormController):
	_name = "form:sale.area.categories"
	_view_name = "sale.area.categories/form"
	_description = "Categories Sale Area"

class ViewModelTreeSaleAreaCategories(ViewModelTreeController):
	_name = "tree:sale.area.categories"
	_view_name = "sale.area.categories/tree"
	_description = "Categories Sale Area"
