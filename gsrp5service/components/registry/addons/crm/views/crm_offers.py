from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelCalendar
from gsrp5service.obj.view import ViewModelO2MCalendar
from gsrp5service.obj.view import ViewModelGraph
from gsrp5service.obj.view import ViewModelO2MGraph
from gsrp5service.obj.view import ViewModelMdx
from gsrp5service.obj.view import ViewModelO2MMdx
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmOffers(ViewModelSearch):
	_name = "model.search.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelFindCrmOffers(ViewModelFind):
	_name = "model.find.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MFormCrmOffers(ViewModelO2MForm):
	_name = "model.o2mform.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelCalendarCrmOffers(ViewModelCalendar):
	_name = "model.calendar.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MCalendarCrmOffers(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelGraphCrmOffers(ViewModelGraph):
	_name = "model.graph.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MGraphCrmOffers(ViewModelO2MGraph):
	_name = "model.o2mgraph.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelMdxCrmOffers(ViewModelMdx):
	_name = "model.mdx.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MMdxCrmOffers(ViewModelO2MMdx):
	_name = "model.o2mmdx.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MListCrmOffers(ViewModelO2MList):
	_name = "model.o2mlist.crm.offers"
	_model = "crm.offers"
	_description = "CRM Offers"
	_columns = ['itype', 'name', 'company', 'fullname', 'market', 'team', 'category_id', 'origin', 'doi', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']
