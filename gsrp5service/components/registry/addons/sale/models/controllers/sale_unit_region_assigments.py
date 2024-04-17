from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleUnitRegionAssigments(ViewModelSearchController):
	_name = "search:sale.unit.region.assigments"
	_view_name = "sale.unit.region.assigments/search"
	_description = "Sale Unit Of Region Assigment"

class ViewModelFindSaleUnitRegionAssigments(ViewModelFindController):
	_name = "find:sale.unit.region.assigments"
	_view_name = "sale.unit.region.assigments/find"
	_description = "Sale Unit Of Region Assigment"

class ViewModelListSaleUnitRegionAssigments(ViewModelListController):
	_name = "list:sale.unit.region.assigments"
	_view_name = "sale.unit.region.assigments/list"
	_description = "Sale Unit Of Region Assigment"

class ViewModelFormModalSaleUnitRegionAssigments(ViewModelFormModalController):
	_name = "form.modal:sale.unit.region.assigments"
	_view_name = "sale.unit.region.assigments/form.modal"
	_description = "Sale Unit Of Region Assigment"

class ViewModelFormSaleUnitRegionAssigments(ViewModelFormController):
	_name = "form:sale.unit.region.assigments"
	_view_name = "sale.unit.region.assigments/form"
	_description = "Sale Unit Of Region Assigment"
