from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmUnitRegionAssigments(ViewModelSearchController):
	_name = "search:crm.unit.region.assigments"
	_view_name = "crm.unit.region.assigments/search"
	_description = "CRM Unit Of Region Assigment"

class ViewModelFindCrmUnitRegionAssigments(ViewModelFindController):
	_name = "find:crm.unit.region.assigments"
	_view_name = "crm.unit.region.assigments/find"
	_description = "CRM Unit Of Region Assigment"

class ViewModelListCrmUnitRegionAssigments(ViewModelListController):
	_name = "list:crm.unit.region.assigments"
	_view_name = "crm.unit.region.assigments/list"
	_description = "CRM Unit Of Region Assigment"

class ViewModelFormModalCrmUnitRegionAssigments(ViewModelFormModalController):
	_name = "form.modal:crm.unit.region.assigments"
	_view_name = "crm.unit.region.assigments/form.modal"
	_description = "CRM Unit Of Region Assigment"

class ViewModelFormCrmUnitRegionAssigments(ViewModelFormController):
	_name = "form:crm.unit.region.assigments"
	_view_name = "crm.unit.region.assigments/form"
	_description = "CRM Unit Of Region Assigment"
