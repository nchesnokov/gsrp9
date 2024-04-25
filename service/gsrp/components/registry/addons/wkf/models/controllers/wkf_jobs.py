from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchWkfJobs(ViewModelSearchController):
	_name = "search:wkf.jobs"
	_view_name = "wkf.jobs/search"
	_description = "Workflow Jobs"

class ViewModelFindWkfJobs(ViewModelFindController):
	_name = "find:wkf.jobs"
	_view_name = "wkf.jobs/find"
	_description = "Workflow Jobs"

class ViewModelListWkfJobs(ViewModelListController):
	_name = "list:wkf.jobs"
	_view_name = "wkf.jobs/list"
	_description = "Workflow Jobs"

class ViewModelFormModalWkfJobs(ViewModelFormModalController):
	_name = "form.modal:wkf.jobs"
	_view_name = "wkf.jobs/form.modal"
	_description = "Workflow Jobs"

class ViewModelFormWkfJobs(ViewModelFormController):
	_name = "form:wkf.jobs"
	_view_name = "wkf.jobs/form"
	_description = "Workflow Jobs"

class ViewModelGanttWkfJobs(ViewModelGanttController):
	_name = "gantt:wkf.jobs"
	_view_name = "wkf.jobs/gantt"
	_description = "Workflow Jobs"

class ViewModelScheduleWkfJobs(ViewModelScheduleController):
	_name = "schedule:wkf.jobs"
	_view_name = "wkf.jobs/schedule"
	_description = "Workflow Jobs"

class ViewModelKanbanWkfJobs(ViewModelKanbanController):
	_name = "kanban:wkf.jobs"
	_view_name = "wkf.jobs/kanban"
	_description = "Workflow Jobs"

class ViewModelTreeWkfJobs(ViewModelTreeController):
	_name = "tree:wkf.jobs"
	_view_name = "wkf.jobs/tree"
	_description = "Workflow Jobs"
