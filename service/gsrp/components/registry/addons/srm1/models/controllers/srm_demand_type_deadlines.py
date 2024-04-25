from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandTypeDeadlines(ViewModelFindController):
	_name = "find:srm.demand.type.deadlines"
	_view_name = "srm.demand.type.deadlines/find"
	_description = "Deadlines SRM Demand Types"

class ViewModelO2MFormSrmDemandTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.type.deadlines"
	_view_name = "srm.demand.type.deadlines/o2m-form"
	_description = "Deadlines SRM Demand Types"

class ViewModelO2MListSrmDemandTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.type.deadlines"
	_view_name = "srm.demand.type.deadlines/o2m-list"
	_description = "Deadlines SRM Demand Types"
