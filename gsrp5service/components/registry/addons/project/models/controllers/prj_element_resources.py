from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPrjElementResources(ViewModelFindController):
	_name = "find:prj.element.resources"
	_view_name = "prj.element.resources/find"
	_description = "Project Element Resources"

class ViewModelO2MFormPrjElementResources(ViewModelO2MFormController):
	_name = "o2m-form:prj.element.resources"
	_view_name = "prj.element.resources/o2m-form"
	_description = "Project Element Resources"

class ViewModelO2MListPrjElementResources(ViewModelO2MListController):
	_name = "o2m-list:prj.element.resources"
	_view_name = "prj.element.resources/o2m-list"
	_description = "Project Element Resources"
