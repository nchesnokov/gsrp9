from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelKanbanController

class ViewModelSearchHcmJob(ViewModelSearchController):
	_name = "search:hcm.job"
	_view_name = "hcm.job/search"
	_description = "Job Position"

class ViewModelFindHcmJob(ViewModelFindController):
	_name = "find:hcm.job"
	_view_name = "hcm.job/find"
	_description = "Job Position"

class ViewModelListHcmJob(ViewModelListController):
	_name = "list:hcm.job"
	_view_name = "hcm.job/list"
	_description = "Job Position"

class ViewModelFormModalHcmJob(ViewModelFormModalController):
	_name = "form.modal:hcm.job"
	_view_name = "hcm.job/form.modal"
	_description = "Job Position"

class ViewModelFormHcmJob(ViewModelFormController):
	_name = "form:hcm.job"
	_view_name = "hcm.job/form"
	_description = "Job Position"

class ViewModelKanbanHcmJob(ViewModelKanbanController):
	_name = "kanban:hcm.job"
	_view_name = "hcm.job/kanban"
	_description = "Job Position"
