from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestTypeDeadlines(ViewModelFindController):
	_name = "find:srm.request.type.deadlines"
	_view_name = "srm.request.type.deadlines/find"
	_description = "Deadlines SRM Request Types"

class ViewModelO2MFormSrmRequestTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.type.deadlines"
	_view_name = "srm.request.type.deadlines/o2m-form"
	_description = "Deadlines SRM Request Types"

class ViewModelO2MListSrmRequestTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.request.type.deadlines"
	_view_name = "srm.request.type.deadlines/o2m-list"
	_description = "Deadlines SRM Request Types"
