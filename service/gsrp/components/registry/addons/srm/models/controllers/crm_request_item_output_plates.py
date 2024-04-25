from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestItemOutputPlates(ViewModelFindController):
	_name = "find:crm.request.item.output.plates"
	_view_name = "crm.request.item.output.plates/find"
	_description = "CRM Request Item Output Plates"

class ViewModelO2MFormCrmRequestItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.item.output.plates"
	_view_name = "crm.request.item.output.plates/o2m-form"
	_description = "CRM Request Item Output Plates"

class ViewModelO2MListCrmRequestItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:crm.request.item.output.plates"
	_view_name = "crm.request.item.output.plates/o2m-list"
	_description = "CRM Request Item Output Plates"
