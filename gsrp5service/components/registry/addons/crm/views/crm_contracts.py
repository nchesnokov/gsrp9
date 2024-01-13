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

class ViewModelSearchCrmContracts(ViewModelSearch):
	_name = "model.search.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelFindCrmContracts(ViewModelFind):
	_name = "model.find.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MFormCrmContracts(ViewModelO2MForm):
	_name = "model.o2mform.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'items', 'pricing', 'roles', 'texts', 'plates', 'payments', 'note']

class ViewModelGanttCrmContracts(ViewModelGantt):
	_name = "model.gantt.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MGanttCrmContracts(ViewModelO2MGantt):
	_name = "model.o2mgantt.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelScheduleCrmContracts(ViewModelSchedule):
	_name = "model.schedule.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MScheduleCrmContracts(ViewModelO2MSchedule):
	_name = "model.o2mschedule.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelCalendarCrmContracts(ViewModelCalendar):
	_name = "model.calendar.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MCalendarCrmContracts(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelGraphCrmContracts(ViewModelGraph):
	_name = "model.graph.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MGraphCrmContracts(ViewModelO2MGraph):
	_name = "model.o2mgraph.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelKanbanCrmContracts(ViewModelKanban):
	_name = "model.kanban.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MKanbanCrmContracts(ViewModelO2MKanban):
	_name = "model.o2mkanban.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelMdxCrmContracts(ViewModelMdx):
	_name = "model.mdx.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MMdxCrmContracts(ViewModelO2MMdx):
	_name = "model.o2mmdx.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MListCrmContracts(ViewModelO2MList):
	_name = "model.o2mlist.crm.contracts"
	_model = "crm.contracts"
	_description = "CRM Contracts"
	_columns = ['otype', 'grp_contract_id', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'items', 'pricing', 'roles', 'texts', 'plates', 'payments']
