from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartTypePlates(ViewModelFindController):
	_name = "find:srm.part.type.plates"
	_view_name = "srm.part.type.plates/find"
	_description = "SRM Part Plates"

class ViewModelO2MFormSrmPartTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.type.plates"
	_view_name = "srm.part.type.plates/o2m-form"
	_description = "SRM Part Plates"

class ViewModelO2MListSrmPartTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.part.type.plates"
	_view_name = "srm.part.type.plates/o2m-list"
	_description = "SRM Part Plates"
