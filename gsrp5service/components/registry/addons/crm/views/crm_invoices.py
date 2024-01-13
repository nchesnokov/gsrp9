from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelCalendar
from gsrp5service.obj.view import ViewModelO2MCalendar
from gsrp5service.obj.view import ViewModelGraph
from gsrp5service.obj.view import ViewModelO2MGraph
from gsrp5service.obj.view import ViewModelKanban
from gsrp5service.obj.view import ViewModelO2MKanban
from gsrp5service.obj.view import ViewModelMdx
from gsrp5service.obj.view import ViewModelO2MMdx
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmInvoices(ViewModelSearch):
	_name = "model.search.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelFindCrmInvoices(ViewModelFind):
	_name = "model.find.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MFormCrmInvoices(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelCalendarCrmInvoices(ViewModelCalendar):
	_name = "model.calendar.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MCalendarCrmInvoices(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelGraphCrmInvoices(ViewModelGraph):
	_name = "model.graph.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MGraphCrmInvoices(ViewModelO2MGraph):
	_name = "model.o2mgraph.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelKanbanCrmInvoices(ViewModelKanban):
	_name = "model.kanban.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MKanbanCrmInvoices(ViewModelO2MKanban):
	_name = "model.o2mkanban.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelMdxCrmInvoices(ViewModelMdx):
	_name = "model.mdx.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MMdxCrmInvoices(ViewModelO2MMdx):
	_name = "model.o2mmdx.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MListCrmInvoices(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoices"
	_model = "crm.invoices"
	_description = "CRM Invoices"
	_columns = ['itype', 'name', 'company', 'fullname', 'market_id', 'team_id', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts']
