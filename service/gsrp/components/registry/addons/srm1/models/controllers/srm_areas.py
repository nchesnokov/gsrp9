from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmAreas(ViewModelSearchController):
	_name = "search:srm.areas"
	_view_name = "srm.areas/search"
	_description = "SRM Areas"

class ViewModelFindSrmAreas(ViewModelFindController):
	_name = "find:srm.areas"
	_view_name = "srm.areas/find"
	_description = "SRM Areas"

class ViewModelListSrmAreas(ViewModelListController):
	_name = "list:srm.areas"
	_view_name = "srm.areas/list"
	_description = "SRM Areas"

class ViewModelFormModalSrmAreas(ViewModelFormModalController):
	_name = "form.modal:srm.areas"
	_view_name = "srm.areas/form.modal"
	_description = "SRM Areas"

class ViewModelFormSrmAreas(ViewModelFormController):
	_name = "form:srm.areas"
	_view_name = "srm.areas/form"
	_description = "SRM Areas"
