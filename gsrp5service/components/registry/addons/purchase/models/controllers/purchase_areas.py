from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseAreas(ViewModelSearchController):
	_name = "search:purchase.areas"
	_view_name = "purchase.areas/search"
	_description = "Purchase Areas"

class ViewModelFindPurchaseAreas(ViewModelFindController):
	_name = "find:purchase.areas"
	_view_name = "purchase.areas/find"
	_description = "Purchase Areas"

class ViewModelListPurchaseAreas(ViewModelListController):
	_name = "list:purchase.areas"
	_view_name = "purchase.areas/list"
	_description = "Purchase Areas"

class ViewModelFormModalPurchaseAreas(ViewModelFormModalController):
	_name = "form.modal:purchase.areas"
	_view_name = "purchase.areas/form.modal"
	_description = "Purchase Areas"

class ViewModelFormPurchaseAreas(ViewModelFormController):
	_name = "form:purchase.areas"
	_view_name = "purchase.areas/form"
	_description = "Purchase Areas"
