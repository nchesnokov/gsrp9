from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseUnits(ViewModelSearchController):
	_name = "search:purchase.units"
	_view_name = "purchase.units/search"
	_description = "Purchase Units"

class ViewModelFindPurchaseUnits(ViewModelFindController):
	_name = "find:purchase.units"
	_view_name = "purchase.units/find"
	_description = "Purchase Units"

class ViewModelListPurchaseUnits(ViewModelListController):
	_name = "list:purchase.units"
	_view_name = "purchase.units/list"
	_description = "Purchase Units"

class ViewModelM2MListMdCompany(ViewModelM2MListController):
	_name = "m2mlist:md.company"
	_view_name = "md.company/m2mlist"
	_description = "Purchase Units"

class ViewModelFormModalPurchaseUnits(ViewModelFormModalController):
	_name = "form.modal:purchase.units"
	_view_name = "purchase.units/form.modal"
	_description = "Purchase Units"

class ViewModelFormPurchaseUnits(ViewModelFormController):
	_name = "form:purchase.units"
	_view_name = "purchase.units/form"
	_description = "Purchase Units"
