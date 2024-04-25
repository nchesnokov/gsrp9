from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmDivisions(ViewModelSearchController):
	_name = "search:srm.divisions"
	_view_name = "srm.divisions/search"
	_description = "SRM Divisions"

class ViewModelFindSrmDivisions(ViewModelFindController):
	_name = "find:srm.divisions"
	_view_name = "srm.divisions/find"
	_description = "SRM Divisions"

class ViewModelListSrmDivisions(ViewModelListController):
	_name = "list:srm.divisions"
	_view_name = "srm.divisions/list"
	_description = "SRM Divisions"

class ViewModelFormModalSrmDivisions(ViewModelFormModalController):
	_name = "form.modal:srm.divisions"
	_view_name = "srm.divisions/form.modal"
	_description = "SRM Divisions"

class ViewModelFormSrmDivisions(ViewModelFormController):
	_name = "form:srm.divisions"
	_view_name = "srm.divisions/form"
	_description = "SRM Divisions"
