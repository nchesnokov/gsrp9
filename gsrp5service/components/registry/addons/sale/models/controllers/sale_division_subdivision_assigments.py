from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleDivisionSubdivisionAssigments(ViewModelSearchController):
	_name = "search:sale.division.subdivision.assigments"
	_view_name = "sale.division.subdivision.assigments/search"
	_description = "Sale Division Of Subdivision Assigment"

class ViewModelFindSaleDivisionSubdivisionAssigments(ViewModelFindController):
	_name = "find:sale.division.subdivision.assigments"
	_view_name = "sale.division.subdivision.assigments/find"
	_description = "Sale Division Of Subdivision Assigment"

class ViewModelListSaleDivisionSubdivisionAssigments(ViewModelListController):
	_name = "list:sale.division.subdivision.assigments"
	_view_name = "sale.division.subdivision.assigments/list"
	_description = "Sale Division Of Subdivision Assigment"

class ViewModelFormModalSaleDivisionSubdivisionAssigments(ViewModelFormModalController):
	_name = "form.modal:sale.division.subdivision.assigments"
	_view_name = "sale.division.subdivision.assigments/form.modal"
	_description = "Sale Division Of Subdivision Assigment"

class ViewModelFormSaleDivisionSubdivisionAssigments(ViewModelFormController):
	_name = "form:sale.division.subdivision.assigments"
	_view_name = "sale.division.subdivision.assigments/form"
	_description = "Sale Division Of Subdivision Assigment"
