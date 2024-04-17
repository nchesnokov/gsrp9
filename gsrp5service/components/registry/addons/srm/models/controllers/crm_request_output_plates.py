from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestOutputPlates(ViewModelFindController):
	_name = "find:crm.request.output.plates"
	_view_name = "crm.request.output.plates/find"
	_description = "CRM Request Output Plates"

class ViewModelO2MFormCrmRequestOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.output.plates"
	_view_name = "crm.request.output.plates/o2m-form"
	_description = "CRM Request Output Plates"

class ViewModelO2MListCrmRequestOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:crm.request.output.plates"
	_view_name = "crm.request.output.plates/o2m-list"
	_description = "CRM Request Output Plates"
