from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseTypeDeadlines(ViewModelFindController):
	_name = "find:srm.response.type.deadlines"
	_view_name = "srm.response.type.deadlines/find"
	_description = "Deadlines SRM Response Types"

class ViewModelO2MFormSrmResponseTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.type.deadlines"
	_view_name = "srm.response.type.deadlines/o2m-form"
	_description = "Deadlines SRM Response Types"

class ViewModelO2MListSrmResponseTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.response.type.deadlines"
	_view_name = "srm.response.type.deadlines/o2m-list"
	_description = "Deadlines SRM Response Types"
