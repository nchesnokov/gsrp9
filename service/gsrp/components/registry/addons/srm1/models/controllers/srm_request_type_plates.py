from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestTypePlates(ViewModelFindController):
	_name = "find:srm.request.type.plates"
	_view_name = "srm.request.type.plates/find"
	_description = "SRM Request Plates"

class ViewModelO2MFormSrmRequestTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.type.plates"
	_view_name = "srm.request.type.plates/o2m-form"
	_description = "SRM Request Plates"

class ViewModelO2MListSrmRequestTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.request.type.plates"
	_view_name = "srm.request.type.plates/o2m-list"
	_description = "SRM Request Plates"
