from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleRegions(ViewModelSearchController):
	_name = "search:sale.regions"
	_view_name = "sale.regions/search"
	_description = "Sale Regions"

class ViewModelFindSaleRegions(ViewModelFindController):
	_name = "find:sale.regions"
	_view_name = "sale.regions/find"
	_description = "Sale Regions"

class ViewModelListSaleRegions(ViewModelListController):
	_name = "list:sale.regions"
	_view_name = "sale.regions/list"
	_description = "Sale Regions"

class ViewModelFormModalSaleRegions(ViewModelFormModalController):
	_name = "form.modal:sale.regions"
	_view_name = "sale.regions/form.modal"
	_description = "Sale Regions"

class ViewModelFormSaleRegions(ViewModelFormController):
	_name = "form:sale.regions"
	_view_name = "sale.regions/form"
	_description = "Sale Regions"
