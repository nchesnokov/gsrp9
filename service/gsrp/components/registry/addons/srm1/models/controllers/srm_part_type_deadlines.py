from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartTypeDeadlines(ViewModelFindController):
	_name = "find:srm.part.type.deadlines"
	_view_name = "srm.part.type.deadlines/find"
	_description = "Deadlines SRM Part Types"

class ViewModelO2MFormSrmPartTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.type.deadlines"
	_view_name = "srm.part.type.deadlines/o2m-form"
	_description = "Deadlines SRM Part Types"

class ViewModelO2MListSrmPartTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.part.type.deadlines"
	_view_name = "srm.part.type.deadlines/o2m-list"
	_description = "Deadlines SRM Part Types"
