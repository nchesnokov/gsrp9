from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractTypeDeadlines(ViewModelFindController):
	_name = "find:srm.contract.type.deadlines"
	_view_name = "srm.contract.type.deadlines/find"
	_description = "Deadlines SRM Contract Types"

class ViewModelO2MFormSrmContractTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.type.deadlines"
	_view_name = "srm.contract.type.deadlines/o2m-form"
	_description = "Deadlines SRM Contract Types"

class ViewModelO2MListSrmContractTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.type.deadlines"
	_view_name = "srm.contract.type.deadlines/o2m-list"
	_description = "Deadlines SRM Contract Types"
