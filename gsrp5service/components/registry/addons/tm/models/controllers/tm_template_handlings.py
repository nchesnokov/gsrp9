from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindTmTemplateHandlings(ViewModelFindController):
	_name = "find:tm.template.handlings"
	_view_name = "tm.template.handlings/find"
	_description = "Template Handlings"

class ViewModelO2MFormTmTemplateHandlings(ViewModelO2MFormController):
	_name = "o2m-form:tm.template.handlings"
	_view_name = "tm.template.handlings/o2m-form"
	_description = "Template Handlings"

class ViewModelO2MListTmTemplateHandlings(ViewModelO2MListController):
	_name = "o2m-list:tm.template.handlings"
	_view_name = "tm.template.handlings/o2m-list"
	_description = "Template Handlings"
