from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmUnits(ViewModelSearchController):
	_name = "search:srm.units"
	_view_name = "srm.units/search"
	_description = "SRM Units"

class ViewModelFindSrmUnits(ViewModelFindController):
	_name = "find:srm.units"
	_view_name = "srm.units/find"
	_description = "SRM Units"

class ViewModelListSrmUnits(ViewModelListController):
	_name = "list:srm.units"
	_view_name = "srm.units/list"
	_description = "SRM Units"

class ViewModelM2MListMdCompany(ViewModelM2MListController):
	_name = "m2mlist:md.company"
	_view_name = "md.company/m2mlist"
	_description = "SRM Units"

class ViewModelFormModalSrmUnits(ViewModelFormModalController):
	_name = "form.modal:srm.units"
	_view_name = "srm.units/form.modal"
	_description = "SRM Units"

class ViewModelFormSrmUnits(ViewModelFormController):
	_name = "form:srm.units"
	_view_name = "srm.units/form"
	_description = "SRM Units"
