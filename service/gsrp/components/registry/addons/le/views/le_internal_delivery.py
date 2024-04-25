from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
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

class ViewModelSearchLeInternalDelivery(ViewModelSearch):
	_name = "model.search.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelFindLeInternalDelivery(ViewModelFind):
	_name = "model.find.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelListLeInternalDelivery(ViewModelList):
	_name = "model.list.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts']

class ViewModelFormModalLeInternalDelivery(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelFormLeInternalDelivery(ViewModelForm):
	_name = "model.form.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelO2MFormLeInternalDelivery(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelCalendarLeInternalDelivery(ViewModelCalendar):
	_name = "model.calendar.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MCalendarLeInternalDelivery(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelGraphLeInternalDelivery(ViewModelGraph):
	_name = "model.graph.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MGraphLeInternalDelivery(ViewModelO2MGraph):
	_name = "model.o2mgraph.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelKanbanLeInternalDelivery(ViewModelKanban):
	_name = "model.kanban.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MKanbanLeInternalDelivery(ViewModelO2MKanban):
	_name = "model.o2mkanban.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelMdxLeInternalDelivery(ViewModelMdx):
	_name = "model.mdx.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MMdxLeInternalDelivery(ViewModelO2MMdx):
	_name = "modelo2mmdx.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MListLeInternalDelivery(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery"
	_model = "le.internal.delivery"
	_description = "Internal Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts']
