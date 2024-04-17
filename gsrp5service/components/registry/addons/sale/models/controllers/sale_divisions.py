from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleDivisions(ViewModelSearchController):
	_name = "search:sale.divisions"
	_view_name = "sale.divisions/search"
	_description = "Sale Divisions"

class ViewModelFindSaleDivisions(ViewModelFindController):
	_name = "find:sale.divisions"
	_view_name = "sale.divisions/find"
	_description = "Sale Divisions"

class ViewModelListSaleDivisions(ViewModelListController):
	_name = "list:sale.divisions"
	_view_name = "sale.divisions/list"
	_description = "Sale Divisions"

class ViewModelFormModalSaleDivisions(ViewModelFormModalController):
	_name = "form.modal:sale.divisions"
	_view_name = "sale.divisions/form.modal"
	_description = "Sale Divisions"

class ViewModelFormSaleDivisions(ViewModelFormController):
	_name = "form:sale.divisions"
	_view_name = "sale.divisions/form"
	_description = "Sale Divisions"
