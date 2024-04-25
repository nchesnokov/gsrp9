from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleUnitAreaAssigments(ViewModelSearchController):
	_name = "search:sale.unit.area.assigments"
	_view_name = "sale.unit.area.assigments/search"
	_description = "Sale Unit Of Area Assigment"

class ViewModelFindSaleUnitAreaAssigments(ViewModelFindController):
	_name = "find:sale.unit.area.assigments"
	_view_name = "sale.unit.area.assigments/find"
	_description = "Sale Unit Of Area Assigment"

class ViewModelListSaleUnitAreaAssigments(ViewModelListController):
	_name = "list:sale.unit.area.assigments"
	_view_name = "sale.unit.area.assigments/list"
	_description = "Sale Unit Of Area Assigment"

class ViewModelFormModalSaleUnitAreaAssigments(ViewModelFormModalController):
	_name = "form.modal:sale.unit.area.assigments"
	_view_name = "sale.unit.area.assigments/form.modal"
	_description = "Sale Unit Of Area Assigment"

class ViewModelFormSaleUnitAreaAssigments(ViewModelFormController):
	_name = "form:sale.unit.area.assigments"
	_view_name = "sale.unit.area.assigments/form"
	_description = "Sale Unit Of Area Assigment"
