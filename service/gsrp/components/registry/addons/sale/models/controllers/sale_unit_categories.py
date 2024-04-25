from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleUnitCategories(ViewModelSearchController):
	_name = "search:sale.unit.categories"
	_view_name = "sale.unit.categories/search"
	_description = "Categories Sale Unit"

class ViewModelFindSaleUnitCategories(ViewModelFindController):
	_name = "find:sale.unit.categories"
	_view_name = "sale.unit.categories/find"
	_description = "Categories Sale Unit"

class ViewModelListSaleUnitCategories(ViewModelListController):
	_name = "list:sale.unit.categories"
	_view_name = "sale.unit.categories/list"
	_description = "Categories Sale Unit"

class ViewModelFormModalSaleUnitCategories(ViewModelFormModalController):
	_name = "form.modal:sale.unit.categories"
	_view_name = "sale.unit.categories/form.modal"
	_description = "Categories Sale Unit"

class ViewModelFormSaleUnitCategories(ViewModelFormController):
	_name = "form:sale.unit.categories"
	_view_name = "sale.unit.categories/form"
	_description = "Categories Sale Unit"

class ViewModelTreeSaleUnitCategories(ViewModelTreeController):
	_name = "tree:sale.unit.categories"
	_view_name = "sale.unit.categories/tree"
	_description = "Categories Sale Unit"
