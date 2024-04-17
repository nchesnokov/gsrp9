from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseRegions(ViewModelSearchController):
	_name = "search:purchase.regions"
	_view_name = "purchase.regions/search"
	_description = "Purchase Regions"

class ViewModelFindPurchaseRegions(ViewModelFindController):
	_name = "find:purchase.regions"
	_view_name = "purchase.regions/find"
	_description = "Purchase Regions"

class ViewModelListPurchaseRegions(ViewModelListController):
	_name = "list:purchase.regions"
	_view_name = "purchase.regions/list"
	_description = "Purchase Regions"

class ViewModelFormModalPurchaseRegions(ViewModelFormModalController):
	_name = "form.modal:purchase.regions"
	_view_name = "purchase.regions/form.modal"
	_description = "Purchase Regions"

class ViewModelFormPurchaseRegions(ViewModelFormController):
	_name = "form:purchase.regions"
	_view_name = "purchase.regions/form"
	_description = "Purchase Regions"
