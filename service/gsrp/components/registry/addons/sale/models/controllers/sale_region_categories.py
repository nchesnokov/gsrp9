from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleRegionCategories(ViewModelSearchController):
	_name = "search:sale.region.categories"
	_view_name = "sale.region.categories/search"
	_description = "Categories Sale Region"

class ViewModelFindSaleRegionCategories(ViewModelFindController):
	_name = "find:sale.region.categories"
	_view_name = "sale.region.categories/find"
	_description = "Categories Sale Region"

class ViewModelListSaleRegionCategories(ViewModelListController):
	_name = "list:sale.region.categories"
	_view_name = "sale.region.categories/list"
	_description = "Categories Sale Region"

class ViewModelFormModalSaleRegionCategories(ViewModelFormModalController):
	_name = "form.modal:sale.region.categories"
	_view_name = "sale.region.categories/form.modal"
	_description = "Categories Sale Region"

class ViewModelFormSaleRegionCategories(ViewModelFormController):
	_name = "form:sale.region.categories"
	_view_name = "sale.region.categories/form"
	_description = "Categories Sale Region"

class ViewModelTreeSaleRegionCategories(ViewModelTreeController):
	_name = "tree:sale.region.categories"
	_view_name = "sale.region.categories/tree"
	_description = "Categories Sale Region"
