from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseDivisions(ViewModelSearchController):
	_name = "search:purchase.divisions"
	_view_name = "purchase.divisions/search"
	_description = "Purchase Divisions"

class ViewModelFindPurchaseDivisions(ViewModelFindController):
	_name = "find:purchase.divisions"
	_view_name = "purchase.divisions/find"
	_description = "Purchase Divisions"

class ViewModelListPurchaseDivisions(ViewModelListController):
	_name = "list:purchase.divisions"
	_view_name = "purchase.divisions/list"
	_description = "Purchase Divisions"

class ViewModelFormModalPurchaseDivisions(ViewModelFormModalController):
	_name = "form.modal:purchase.divisions"
	_view_name = "purchase.divisions/form.modal"
	_description = "Purchase Divisions"

class ViewModelFormPurchaseDivisions(ViewModelFormController):
	_name = "form:purchase.divisions"
	_view_name = "purchase.divisions/form"
	_description = "Purchase Divisions"
