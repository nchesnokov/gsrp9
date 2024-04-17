from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleSubdivisions(ViewModelSearchController):
	_name = "search:sale.subdivisions"
	_view_name = "sale.subdivisions/search"
	_description = "Sale Subdivisions"

class ViewModelFindSaleSubdivisions(ViewModelFindController):
	_name = "find:sale.subdivisions"
	_view_name = "sale.subdivisions/find"
	_description = "Sale Subdivisions"

class ViewModelListSaleSubdivisions(ViewModelListController):
	_name = "list:sale.subdivisions"
	_view_name = "sale.subdivisions/list"
	_description = "Sale Subdivisions"

class ViewModelFormModalSaleSubdivisions(ViewModelFormModalController):
	_name = "form.modal:sale.subdivisions"
	_view_name = "sale.subdivisions/form.modal"
	_description = "Sale Subdivisions"

class ViewModelFormSaleSubdivisions(ViewModelFormController):
	_name = "form:sale.subdivisions"
	_view_name = "sale.subdivisions/form"
	_description = "Sale Subdivisions"
