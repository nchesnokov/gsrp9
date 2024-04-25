from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchCrmGroupContracts(ViewModelSearchController):
	_name = "search:crm.group.contracts"
	_view_name = "crm.group.contracts/search"
	_description = "CRM Group Contracts"

class ViewModelFindCrmGroupContracts(ViewModelFindController):
	_name = "find:crm.group.contracts"
	_view_name = "crm.group.contracts/find"
	_description = "CRM Group Contracts"

class ViewModelListCrmGroupContracts(ViewModelListController):
	_name = "list:crm.group.contracts"
	_view_name = "crm.group.contracts/list"
	_description = "CRM Group Contracts"

class ViewModelFormModalCrmGroupContracts(ViewModelFormModalController):
	_name = "form.modal:crm.group.contracts"
	_view_name = "crm.group.contracts/form.modal"
	_description = "CRM Group Contracts"

class ViewModelFormCrmGroupContracts(ViewModelFormController):
	_name = "form:crm.group.contracts"
	_view_name = "crm.group.contracts/form"
	_description = "CRM Group Contracts"

class ViewModelGanttCrmGroupContracts(ViewModelGanttController):
	_name = "gantt:crm.group.contracts"
	_view_name = "crm.group.contracts/gantt"
	_description = "CRM Group Contracts"

class ViewModelScheduleCrmGroupContracts(ViewModelScheduleController):
	_name = "schedule:crm.group.contracts"
	_view_name = "crm.group.contracts/schedule"
	_description = "CRM Group Contracts"

class ViewModelCalendarCrmGroupContracts(ViewModelCalendarController):
	_name = "calendar:crm.group.contracts"
	_view_name = "crm.group.contracts/calendar"
	_description = "CRM Group Contracts"

class ViewModelGraphCrmGroupContracts(ViewModelGraphController):
	_name = "graph:crm.group.contracts"
	_view_name = "crm.group.contracts/graph"
	_description = "CRM Group Contracts"

class ViewModelKanbanCrmGroupContracts(ViewModelKanbanController):
	_name = "kanban:crm.group.contracts"
	_view_name = "crm.group.contracts/kanban"
	_description = "CRM Group Contracts"

class ViewModelMdxCrmGroupContracts(ViewModelMdxController):
	_name = "mdx:crm.group.contracts"
	_view_name = "crm.group.contracts/mdx"
	_description = "CRM Group Contracts"
