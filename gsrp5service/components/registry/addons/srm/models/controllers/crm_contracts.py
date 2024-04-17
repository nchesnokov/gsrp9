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

class ViewModelSearchCrmContracts(ViewModelSearchController):
	_name = "search:crm.contracts"
	_view_name = "crm.contracts/search"
	_description = "CRM Contracts"

class ViewModelFindCrmContracts(ViewModelFindController):
	_name = "find:crm.contracts"
	_view_name = "crm.contracts/find"
	_description = "CRM Contracts"

class ViewModelListCrmContracts(ViewModelListController):
	_name = "list:crm.contracts"
	_view_name = "crm.contracts/list"
	_description = "CRM Contracts"

class ViewModelFormModalCrmContracts(ViewModelFormModalController):
	_name = "form.modal:crm.contracts"
	_view_name = "crm.contracts/form.modal"
	_description = "CRM Contracts"

class ViewModelFormCrmContracts(ViewModelFormController):
	_name = "form:crm.contracts"
	_view_name = "crm.contracts/form"
	_description = "CRM Contracts"

class ViewModelGanttCrmContracts(ViewModelGanttController):
	_name = "gantt:crm.contracts"
	_view_name = "crm.contracts/gantt"
	_description = "CRM Contracts"

class ViewModelScheduleCrmContracts(ViewModelScheduleController):
	_name = "schedule:crm.contracts"
	_view_name = "crm.contracts/schedule"
	_description = "CRM Contracts"

class ViewModelCalendarCrmContracts(ViewModelCalendarController):
	_name = "calendar:crm.contracts"
	_view_name = "crm.contracts/calendar"
	_description = "CRM Contracts"

class ViewModelGraphCrmContracts(ViewModelGraphController):
	_name = "graph:crm.contracts"
	_view_name = "crm.contracts/graph"
	_description = "CRM Contracts"

class ViewModelKanbanCrmContracts(ViewModelKanbanController):
	_name = "kanban:crm.contracts"
	_view_name = "crm.contracts/kanban"
	_description = "CRM Contracts"

class ViewModelMdxCrmContracts(ViewModelMdxController):
	_name = "mdx:crm.contracts"
	_view_name = "crm.contracts/mdx"
	_description = "CRM Contracts"
