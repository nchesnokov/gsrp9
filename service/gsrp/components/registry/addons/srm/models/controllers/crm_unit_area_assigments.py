from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmUnitAreaAssigments(ViewModelSearchController):
	_name = "search:crm.unit.area.assigments"
	_view_name = "crm.unit.area.assigments/search"
	_description = "CRM Unit Of Area Assigment"

class ViewModelFindCrmUnitAreaAssigments(ViewModelFindController):
	_name = "find:crm.unit.area.assigments"
	_view_name = "crm.unit.area.assigments/find"
	_description = "CRM Unit Of Area Assigment"

class ViewModelListCrmUnitAreaAssigments(ViewModelListController):
	_name = "list:crm.unit.area.assigments"
	_view_name = "crm.unit.area.assigments/list"
	_description = "CRM Unit Of Area Assigment"

class ViewModelFormModalCrmUnitAreaAssigments(ViewModelFormModalController):
	_name = "form.modal:crm.unit.area.assigments"
	_view_name = "crm.unit.area.assigments/form.modal"
	_description = "CRM Unit Of Area Assigment"

class ViewModelFormCrmUnitAreaAssigments(ViewModelFormController):
	_name = "form:crm.unit.area.assigments"
	_view_name = "crm.unit.area.assigments/form"
	_description = "CRM Unit Of Area Assigment"
