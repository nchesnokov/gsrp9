from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseSubdivisions(ViewModelSearchController):
	_name = "search:purchase.subdivisions"
	_view_name = "purchase.subdivisions/search"
	_description = "Purchase Subdivisions"

class ViewModelFindPurchaseSubdivisions(ViewModelFindController):
	_name = "find:purchase.subdivisions"
	_view_name = "purchase.subdivisions/find"
	_description = "Purchase Subdivisions"

class ViewModelListPurchaseSubdivisions(ViewModelListController):
	_name = "list:purchase.subdivisions"
	_view_name = "purchase.subdivisions/list"
	_description = "Purchase Subdivisions"

class ViewModelFormModalPurchaseSubdivisions(ViewModelFormModalController):
	_name = "form.modal:purchase.subdivisions"
	_view_name = "purchase.subdivisions/form.modal"
	_description = "Purchase Subdivisions"

class ViewModelFormPurchaseSubdivisions(ViewModelFormController):
	_name = "form:purchase.subdivisions"
	_view_name = "purchase.subdivisions/form"
	_description = "Purchase Subdivisions"
