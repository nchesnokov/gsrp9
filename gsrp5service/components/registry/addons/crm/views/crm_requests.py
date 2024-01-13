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
from gsrp5service.obj.view import ViewModelMdx
from gsrp5service.obj.view import ViewModelO2MMdx
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmRequests(ViewModelSearch):
	_name = "model.search.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelFindCrmRequests(ViewModelFind):
	_name = "model.find.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MFormCrmRequests(ViewModelO2MForm):
	_name = "model.o2mform.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'items', 'pricing', 'roles', 'texts', 'plates', 'payments', 'note']

class ViewModelGanttCrmRequests(ViewModelGantt):
	_name = "model.gantt.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MGanttCrmRequests(ViewModelO2MGantt):
	_name = "model.o2mgantt.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelScheduleCrmRequests(ViewModelSchedule):
	_name = "model.schedule.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MScheduleCrmRequests(ViewModelO2MSchedule):
	_name = "model.o2mschedule.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelCalendarCrmRequests(ViewModelCalendar):
	_name = "model.calendar.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MCalendarCrmRequests(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelGraphCrmRequests(ViewModelGraph):
	_name = "model.graph.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MGraphCrmRequests(ViewModelO2MGraph):
	_name = "model.o2mgraph.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelMdxCrmRequests(ViewModelMdx):
	_name = "model.mdx.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MMdxCrmRequests(ViewModelO2MMdx):
	_name = "model.o2mmdx.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MListCrmRequests(ViewModelO2MList):
	_name = "model.o2mlist.crm.requests"
	_model = "crm.requests"
	_description = "CRM Requests"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'items', 'pricing', 'roles', 'texts', 'plates', 'payments', 'note']
