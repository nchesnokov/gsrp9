from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleAreas(ViewModelSearchController):
	_name = "search:sale.areas"
	_view_name = "sale.areas/search"
	_description = "Sale Areas"

class ViewModelFindSaleAreas(ViewModelFindController):
	_name = "find:sale.areas"
	_view_name = "sale.areas/find"
	_description = "Sale Areas"

class ViewModelListSaleAreas(ViewModelListController):
	_name = "list:sale.areas"
	_view_name = "sale.areas/list"
	_description = "Sale Areas"

class ViewModelFormModalSaleAreas(ViewModelFormModalController):
	_name = "form.modal:sale.areas"
	_view_name = "sale.areas/form.modal"
	_description = "Sale Areas"

class ViewModelFormSaleAreas(ViewModelFormController):
	_name = "form:sale.areas"
	_view_name = "sale.areas/form"
	_description = "Sale Areas"
