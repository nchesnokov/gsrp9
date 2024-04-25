from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmDeadlines(ViewModelSearchController):
	_name = "search:srm.deadlines"
	_view_name = "srm.deadlines/search"
	_description = "SRM Deadlines"

class ViewModelFindSrmDeadlines(ViewModelFindController):
	_name = "find:srm.deadlines"
	_view_name = "srm.deadlines/find"
	_description = "SRM Deadlines"

class ViewModelListSrmDeadlines(ViewModelListController):
	_name = "list:srm.deadlines"
	_view_name = "srm.deadlines/list"
	_description = "SRM Deadlines"

class ViewModelFormModalSrmDeadlines(ViewModelFormModalController):
	_name = "form.modal:srm.deadlines"
	_view_name = "srm.deadlines/form.modal"
	_description = "SRM Deadlines"

class ViewModelFormSrmDeadlines(ViewModelFormController):
	_name = "form:srm.deadlines"
	_view_name = "srm.deadlines/form"
	_description = "SRM Deadlines"
