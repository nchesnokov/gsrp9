from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseTypePlates(ViewModelFindController):
	_name = "find:srm.response.type.plates"
	_view_name = "srm.response.type.plates/find"
	_description = "SRM Response Plates"

class ViewModelO2MFormSrmResponseTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.type.plates"
	_view_name = "srm.response.type.plates/o2m-form"
	_description = "SRM Response Plates"

class ViewModelO2MListSrmResponseTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.response.type.plates"
	_view_name = "srm.response.type.plates/o2m-list"
	_description = "SRM Response Plates"
