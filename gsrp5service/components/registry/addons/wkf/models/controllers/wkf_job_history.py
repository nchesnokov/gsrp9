from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindWkfJobHistory(ViewModelFindController):
	_name = "find:wkf.job.history"
	_view_name = "wkf.job.history/find"
	_description = "Workflow History Job"

class ViewModelO2MFormWkfJobHistory(ViewModelO2MFormController):
	_name = "o2m-form:wkf.job.history"
	_view_name = "wkf.job.history/o2m-form"
	_description = "Workflow History Job"

class ViewModelO2MKanbanWkfJobHistory(ViewModelO2MKanbanController):
	_name = "o2m-kanban:wkf.job.history"
	_view_name = "wkf.job.history/o2m-kanban"
	_description = "Workflow History Job"

class ViewModelO2MListWkfJobHistory(ViewModelO2MListController):
	_name = "o2m-list:wkf.job.history"
	_view_name = "wkf.job.history/o2m-list"
	_description = "Workflow History Job"
