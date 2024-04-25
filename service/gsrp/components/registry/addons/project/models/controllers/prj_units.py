from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjUnits(ViewModelSearchController):
	_name = "search:prj.units"
	_view_name = "prj.units/search"
	_description = "Project Units"

class ViewModelFindPrjUnits(ViewModelFindController):
	_name = "find:prj.units"
	_view_name = "prj.units/find"
	_description = "Project Units"

class ViewModelListPrjUnits(ViewModelListController):
	_name = "list:prj.units"
	_view_name = "prj.units/list"
	_description = "Project Units"

class ViewModelM2MListMdCompany(ViewModelM2MListController):
	_name = "m2mlist:md.company"
	_view_name = "md.company/m2mlist"
	_description = "Project Units"

class ViewModelFormModalPrjUnits(ViewModelFormModalController):
	_name = "form.modal:prj.units"
	_view_name = "prj.units/form.modal"
	_description = "Project Units"

class ViewModelFormPrjUnits(ViewModelFormController):
	_name = "form:prj.units"
	_view_name = "prj.units/form"
	_description = "Project Units"
