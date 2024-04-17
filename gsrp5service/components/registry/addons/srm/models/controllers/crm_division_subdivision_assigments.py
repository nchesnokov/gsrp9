from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmDivisionSubdivisionAssigments(ViewModelSearchController):
	_name = "search:crm.division.subdivision.assigments"
	_view_name = "crm.division.subdivision.assigments/search"
	_description = "CRM Division Of Subdivision Assigment"

class ViewModelFindCrmDivisionSubdivisionAssigments(ViewModelFindController):
	_name = "find:crm.division.subdivision.assigments"
	_view_name = "crm.division.subdivision.assigments/find"
	_description = "CRM Division Of Subdivision Assigment"

class ViewModelListCrmDivisionSubdivisionAssigments(ViewModelListController):
	_name = "list:crm.division.subdivision.assigments"
	_view_name = "crm.division.subdivision.assigments/list"
	_description = "CRM Division Of Subdivision Assigment"

class ViewModelFormModalCrmDivisionSubdivisionAssigments(ViewModelFormModalController):
	_name = "form.modal:crm.division.subdivision.assigments"
	_view_name = "crm.division.subdivision.assigments/form.modal"
	_description = "CRM Division Of Subdivision Assigment"

class ViewModelFormCrmDivisionSubdivisionAssigments(ViewModelFormController):
	_name = "form:crm.division.subdivision.assigments"
	_view_name = "crm.division.subdivision.assigments/form"
	_description = "CRM Division Of Subdivision Assigment"
