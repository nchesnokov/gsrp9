from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelGantt
from gsrp5service.obj.view import ViewModelO2MGantt
from gsrp5service.obj.view import ViewModelSchedule
from gsrp5service.obj.view import ViewModelO2MSchedule
from gsrp5service.obj.view import ViewModelCalendar
from gsrp5service.obj.view import ViewModelO2MCalendar
from gsrp5service.obj.view import ViewModelGraph
from gsrp5service.obj.view import ViewModelO2MGraph
from gsrp5service.obj.view import ViewModelKanban
from gsrp5service.obj.view import ViewModelO2MKanban
from gsrp5service.obj.view import ViewModelMdx
from gsrp5service.obj.view import ViewModelO2MMdx
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmGroupContracts(ViewModelSearch):
	_name = "model.search.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelFindCrmGroupContracts(ViewModelFind):
	_name = "model.find.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MFormCrmGroupContracts(ViewModelO2MForm):
	_name = "model.o2mform.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount', 'contracts', 'note']

class ViewModelGanttCrmGroupContracts(ViewModelGantt):
	_name = "model.gantt.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MGanttCrmGroupContracts(ViewModelO2MGantt):
	_name = "model.o2mgantt.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelScheduleCrmGroupContracts(ViewModelSchedule):
	_name = "model.schedule.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MScheduleCrmGroupContracts(ViewModelO2MSchedule):
	_name = "model.o2mschedule.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelCalendarCrmGroupContracts(ViewModelCalendar):
	_name = "model.calendar.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MCalendarCrmGroupContracts(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelGraphCrmGroupContracts(ViewModelGraph):
	_name = "model.graph.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MGraphCrmGroupContracts(ViewModelO2MGraph):
	_name = "model.o2mgraph.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelKanbanCrmGroupContracts(ViewModelKanban):
	_name = "model.kanban.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MKanbanCrmGroupContracts(ViewModelO2MKanban):
	_name = "model.o2mkanban.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelMdxCrmGroupContracts(ViewModelMdx):
	_name = "model.mdx.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MMdxCrmGroupContracts(ViewModelO2MMdx):
	_name = "model.o2mmdx.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MListCrmGroupContracts(ViewModelO2MList):
	_name = "model.o2mlist.crm.group.contracts"
	_model = "crm.group.contracts"
	_description = "CRM Group Contracts"
	_columns = ['name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'state', 'amount', 'vat_amount', 'total_amount', 'contracts']
