from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseUnitAreaAssigments(ViewModelSearchController):
	_name = "search:purchase.unit.area.assigments"
	_view_name = "purchase.unit.area.assigments/search"
	_description = "Purchase Unit Of Area Assigment"

class ViewModelFindPurchaseUnitAreaAssigments(ViewModelFindController):
	_name = "find:purchase.unit.area.assigments"
	_view_name = "purchase.unit.area.assigments/find"
	_description = "Purchase Unit Of Area Assigment"

class ViewModelListPurchaseUnitAreaAssigments(ViewModelListController):
	_name = "list:purchase.unit.area.assigments"
	_view_name = "purchase.unit.area.assigments/list"
	_description = "Purchase Unit Of Area Assigment"

class ViewModelFormModalPurchaseUnitAreaAssigments(ViewModelFormModalController):
	_name = "form.modal:purchase.unit.area.assigments"
	_view_name = "purchase.unit.area.assigments/form.modal"
	_description = "Purchase Unit Of Area Assigment"

class ViewModelFormPurchaseUnitAreaAssigments(ViewModelFormController):
	_name = "form:purchase.unit.area.assigments"
	_view_name = "purchase.unit.area.assigments/form"
	_description = "Purchase Unit Of Area Assigment"
