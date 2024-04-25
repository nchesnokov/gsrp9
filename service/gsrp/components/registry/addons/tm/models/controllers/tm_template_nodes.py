from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindTmTemplateNodes(ViewModelFindController):
	_name = "find:tm.template.nodes"
	_view_name = "tm.template.nodes/find"
	_description = "Template Nodes"

class ViewModelO2MFormTmTemplateNodes(ViewModelO2MFormController):
	_name = "o2m-form:tm.template.nodes"
	_view_name = "tm.template.nodes/o2m-form"
	_description = "Template Nodes"

class ViewModelO2MListTmTemplateNodes(ViewModelO2MListController):
	_name = "o2m-list:tm.template.nodes"
	_view_name = "tm.template.nodes/o2m-list"
	_description = "Template Nodes"
