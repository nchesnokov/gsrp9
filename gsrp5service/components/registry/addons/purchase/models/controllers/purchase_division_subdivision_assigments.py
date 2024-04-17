from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseDivisionSubdivisionAssigments(ViewModelSearchController):
	_name = "search:purchase.division.subdivision.assigments"
	_view_name = "purchase.division.subdivision.assigments/search"
	_description = "Purchase Division Of Subdivision Assigment"

class ViewModelFindPurchaseDivisionSubdivisionAssigments(ViewModelFindController):
	_name = "find:purchase.division.subdivision.assigments"
	_view_name = "purchase.division.subdivision.assigments/find"
	_description = "Purchase Division Of Subdivision Assigment"

class ViewModelListPurchaseDivisionSubdivisionAssigments(ViewModelListController):
	_name = "list:purchase.division.subdivision.assigments"
	_view_name = "purchase.division.subdivision.assigments/list"
	_description = "Purchase Division Of Subdivision Assigment"

class ViewModelFormModalPurchaseDivisionSubdivisionAssigments(ViewModelFormModalController):
	_name = "form.modal:purchase.division.subdivision.assigments"
	_view_name = "purchase.division.subdivision.assigments/form.modal"
	_description = "Purchase Division Of Subdivision Assigment"

class ViewModelFormPurchaseDivisionSubdivisionAssigments(ViewModelFormController):
	_name = "form:purchase.division.subdivision.assigments"
	_view_name = "purchase.division.subdivision.assigments/form"
	_description = "Purchase Division Of Subdivision Assigment"
