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

class ViewModelSearchCrmOrders(ViewModelSearch):
	_name = "model.search.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelFindCrmOrders(ViewModelFind):
	_name = "model.find.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MFormCrmOrders(ViewModelO2MForm):
	_name = "model.o2mform.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'items', 'pricing', 'roles', 'texts', 'plates', 'payments', 'note']

class ViewModelGanttCrmOrders(ViewModelGantt):
	_name = "model.gantt.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MGanttCrmOrders(ViewModelO2MGantt):
	_name = "model.o2mgantt.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelScheduleCrmOrders(ViewModelSchedule):
	_name = "model.schedule.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MScheduleCrmOrders(ViewModelO2MSchedule):
	_name = "model.o2mschedule.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelCalendarCrmOrders(ViewModelCalendar):
	_name = "model.calendar.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MCalendarCrmOrders(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelGraphCrmOrders(ViewModelGraph):
	_name = "model.graph.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MGraphCrmOrders(ViewModelO2MGraph):
	_name = "model.o2mgraph.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelKanbanCrmOrders(ViewModelKanban):
	_name = "model.kanban.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelO2MKanbanCrmOrders(ViewModelO2MKanban):
	_name = "model.o2mkanban.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'note']

class ViewModelMdxCrmOrders(ViewModelMdx):
	_name = "model.mdx.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MMdxCrmOrders(ViewModelO2MMdx):
	_name = "model.o2mmdx.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob']

class ViewModelO2MListCrmOrders(ViewModelO2MList):
	_name = "model.o2mlist.crm.orders"
	_model = "crm.orders"
	_description = "CRM Orders"
	_columns = ['otype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'manager', 'doo', 'from_date', 'to_date', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'mob', 'items', 'pricing', 'roles', 'texts', 'plates', 'payments']
