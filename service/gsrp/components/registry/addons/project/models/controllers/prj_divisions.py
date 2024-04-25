from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjDivisions(ViewModelSearchController):
	_name = "search:prj.divisions"
	_view_name = "prj.divisions/search"
	_description = "Project Divisions"

class ViewModelFindPrjDivisions(ViewModelFindController):
	_name = "find:prj.divisions"
	_view_name = "prj.divisions/find"
	_description = "Project Divisions"

class ViewModelListPrjDivisions(ViewModelListController):
	_name = "list:prj.divisions"
	_view_name = "prj.divisions/list"
	_description = "Project Divisions"

class ViewModelFormModalPrjDivisions(ViewModelFormModalController):
	_name = "form.modal:prj.divisions"
	_view_name = "prj.divisions/form.modal"
	_description = "Project Divisions"

class ViewModelFormPrjDivisions(ViewModelFormController):
	_name = "form:prj.divisions"
	_view_name = "prj.divisions/form"
	_description = "Project Divisions"
