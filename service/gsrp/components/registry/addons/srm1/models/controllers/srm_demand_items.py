from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandItems(ViewModelFindController):
	_name = "find:srm.demand.items"
	_view_name = "srm.demand.items/find"
	_description = "SRM Demant Item"

class ViewModelO2MFormSrmDemandItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.items"
	_view_name = "srm.demand.items/o2m-form"
	_description = "SRM Demant Item"

class ViewModelO2MListSrmDemandItems(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.items"
	_view_name = "srm.demand.items/o2m-list"
	_description = "SRM Demant Item"
