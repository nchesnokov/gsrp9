from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractTypePlates(ViewModelFindController):
	_name = "find:srm.contract.type.plates"
	_view_name = "srm.contract.type.plates/find"
	_description = "SRM Contract Plates"

class ViewModelO2MFormSrmContractTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.type.plates"
	_view_name = "srm.contract.type.plates/o2m-form"
	_description = "SRM Contract Plates"

class ViewModelO2MListSrmContractTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.type.plates"
	_view_name = "srm.contract.type.plates/o2m-list"
	_description = "SRM Contract Plates"
