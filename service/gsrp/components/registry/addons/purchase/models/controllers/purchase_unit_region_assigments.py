from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseUnitRegionAssigments(ViewModelSearchController):
	_name = "search:purchase.unit.region.assigments"
	_view_name = "purchase.unit.region.assigments/search"
	_description = "Purchase Unit Of Region Assigment"

class ViewModelFindPurchaseUnitRegionAssigments(ViewModelFindController):
	_name = "find:purchase.unit.region.assigments"
	_view_name = "purchase.unit.region.assigments/find"
	_description = "Purchase Unit Of Region Assigment"

class ViewModelListPurchaseUnitRegionAssigments(ViewModelListController):
	_name = "list:purchase.unit.region.assigments"
	_view_name = "purchase.unit.region.assigments/list"
	_description = "Purchase Unit Of Region Assigment"

class ViewModelFormModalPurchaseUnitRegionAssigments(ViewModelFormModalController):
	_name = "form.modal:purchase.unit.region.assigments"
	_view_name = "purchase.unit.region.assigments/form.modal"
	_description = "Purchase Unit Of Region Assigment"

class ViewModelFormPurchaseUnitRegionAssigments(ViewModelFormController):
	_name = "form:purchase.unit.region.assigments"
	_view_name = "purchase.unit.region.assigments/form"
	_description = "Purchase Unit Of Region Assigment"
