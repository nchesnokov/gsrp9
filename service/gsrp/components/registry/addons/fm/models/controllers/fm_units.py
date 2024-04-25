from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFmUnits(ViewModelSearchController):
	_name = "search:fm.units"
	_view_name = "fm.units/search"
	_description = "Financial Management Units"

class ViewModelFindFmUnits(ViewModelFindController):
	_name = "find:fm.units"
	_view_name = "fm.units/find"
	_description = "Financial Management Units"

class ViewModelListFmUnits(ViewModelListController):
	_name = "list:fm.units"
	_view_name = "fm.units/list"
	_description = "Financial Management Units"

class ViewModelM2MListMdCompany(ViewModelM2MListController):
	_name = "m2mlist:md.company"
	_view_name = "md.company/m2mlist"
	_description = "Financial Management Units"

class ViewModelFormModalFmUnits(ViewModelFormModalController):
	_name = "form.modal:fm.units"
	_view_name = "fm.units/form.modal"
	_description = "Financial Management Units"

class ViewModelFormFmUnits(ViewModelFormController):
	_name = "form:fm.units"
	_view_name = "fm.units/form"
	_description = "Financial Management Units"
