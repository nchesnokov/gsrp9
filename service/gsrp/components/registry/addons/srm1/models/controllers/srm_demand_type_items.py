from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandTypeItems(ViewModelFindController):
	_name = "find:srm.demand.type.items"
	_view_name = "srm.demand.type.items/find"
	_description = "Type of SRM Deamnd Items"

class ViewModelO2MFormSrmDemandTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.type.items"
	_view_name = "srm.demand.type.items/o2m-form"
	_description = "Type of SRM Deamnd Items"

class ViewModelO2MListSrmDemandTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.type.items"
	_view_name = "srm.demand.type.items/o2m-list"
	_description = "Type of SRM Deamnd Items"
