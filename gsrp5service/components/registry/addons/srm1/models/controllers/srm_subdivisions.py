from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmSubdivisions(ViewModelSearchController):
	_name = "search:srm.subdivisions"
	_view_name = "srm.subdivisions/search"
	_description = "SRM Subdivisions"

class ViewModelFindSrmSubdivisions(ViewModelFindController):
	_name = "find:srm.subdivisions"
	_view_name = "srm.subdivisions/find"
	_description = "SRM Subdivisions"

class ViewModelListSrmSubdivisions(ViewModelListController):
	_name = "list:srm.subdivisions"
	_view_name = "srm.subdivisions/list"
	_description = "SRM Subdivisions"

class ViewModelFormModalSrmSubdivisions(ViewModelFormModalController):
	_name = "form.modal:srm.subdivisions"
	_view_name = "srm.subdivisions/form.modal"
	_description = "SRM Subdivisions"

class ViewModelFormSrmSubdivisions(ViewModelFormController):
	_name = "form:srm.subdivisions"
	_view_name = "srm.subdivisions/form"
	_description = "SRM Subdivisions"
