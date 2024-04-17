from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleSubdivisionCategories(ViewModelSearchController):
	_name = "search:sale.subdivision.categories"
	_view_name = "sale.subdivision.categories/search"
	_description = "Categories Sale Subdivision"

class ViewModelFindSaleSubdivisionCategories(ViewModelFindController):
	_name = "find:sale.subdivision.categories"
	_view_name = "sale.subdivision.categories/find"
	_description = "Categories Sale Subdivision"

class ViewModelListSaleSubdivisionCategories(ViewModelListController):
	_name = "list:sale.subdivision.categories"
	_view_name = "sale.subdivision.categories/list"
	_description = "Categories Sale Subdivision"

class ViewModelFormModalSaleSubdivisionCategories(ViewModelFormModalController):
	_name = "form.modal:sale.subdivision.categories"
	_view_name = "sale.subdivision.categories/form.modal"
	_description = "Categories Sale Subdivision"

class ViewModelFormSaleSubdivisionCategories(ViewModelFormController):
	_name = "form:sale.subdivision.categories"
	_view_name = "sale.subdivision.categories/form"
	_description = "Categories Sale Subdivision"

class ViewModelTreeSaleSubdivisionCategories(ViewModelTreeController):
	_name = "tree:sale.subdivision.categories"
	_view_name = "sale.subdivision.categories/tree"
	_description = "Categories Sale Subdivision"
