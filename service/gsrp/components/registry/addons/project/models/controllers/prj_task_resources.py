from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPrjTaskResources(ViewModelFindController):
	_name = "find:prj.task.resources"
	_view_name = "prj.task.resources/find"
	_description = "Project Task Resources"

class ViewModelO2MFormPrjTaskResources(ViewModelO2MFormController):
	_name = "o2m-form:prj.task.resources"
	_view_name = "prj.task.resources/o2m-form"
	_description = "Project Task Resources"

class ViewModelO2MListPrjTaskResources(ViewModelO2MListController):
	_name = "o2m-list:prj.task.resources"
	_view_name = "prj.task.resources/o2m-list"
	_description = "Project Task Resources"
