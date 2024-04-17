from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjResource(ViewModelSearchController):
	_name = "search:prj.resource"
	_view_name = "prj.resource/search"
	_description = "Project Resource"

class ViewModelFindPrjResource(ViewModelFindController):
	_name = "find:prj.resource"
	_view_name = "prj.resource/find"
	_description = "Project Resource"

class ViewModelListPrjResource(ViewModelListController):
	_name = "list:prj.resource"
	_view_name = "prj.resource/list"
	_description = "Project Resource"

class ViewModelFormModalPrjResource(ViewModelFormModalController):
	_name = "form.modal:prj.resource"
	_view_name = "prj.resource/form.modal"
	_description = "Project Resource"

class ViewModelFormPrjResource(ViewModelFormController):
	_name = "form:prj.resource"
	_view_name = "prj.resource/form"
	_description = "Project Resource"
