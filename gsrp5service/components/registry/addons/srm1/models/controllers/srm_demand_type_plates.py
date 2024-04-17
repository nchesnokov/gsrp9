from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandTypePlates(ViewModelFindController):
	_name = "find:srm.demand.type.plates"
	_view_name = "srm.demand.type.plates/find"
	_description = "SRM Demand Plates"

class ViewModelO2MFormSrmDemandTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.type.plates"
	_view_name = "srm.demand.type.plates/o2m-form"
	_description = "SRM Demand Plates"

class ViewModelO2MListSrmDemandTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.type.plates"
	_view_name = "srm.demand.type.plates/o2m-list"
	_description = "SRM Demand Plates"
