from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindTmTemplateMaps(ViewModelFindController):
	_name = "find:tm.template.maps"
	_view_name = "tm.template.maps/find"
	_description = "Template Maps"

class ViewModelO2MFormTmTemplateMaps(ViewModelO2MFormController):
	_name = "o2m-form:tm.template.maps"
	_view_name = "tm.template.maps/o2m-form"
	_description = "Template Maps"

class ViewModelO2MListTmTemplateMaps(ViewModelO2MListController):
	_name = "o2m-list:tm.template.maps"
	_view_name = "tm.template.maps/o2m-list"
	_description = "Template Maps"
