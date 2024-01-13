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

class ViewModelSearchLeOutboundDelivery(ViewModelSearch):
	_name = "model.search.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelFindLeOutboundDelivery(ViewModelFind):
	_name = "model.find.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelListLeOutboundDelivery(ViewModelList):
	_name = "model.list.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts']

class ViewModelFormModalLeOutboundDelivery(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelFormLeOutboundDelivery(ViewModelForm):
	_name = "model.form.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelO2MFormLeOutboundDelivery(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelCalendarLeOutboundDelivery(ViewModelCalendar):
	_name = "model.calendar.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MCalendarLeOutboundDelivery(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelGraphLeOutboundDelivery(ViewModelGraph):
	_name = "model.graph.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MGraphLeOutboundDelivery(ViewModelO2MGraph):
	_name = "model.o2mgraph.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelKanbanLeOutboundDelivery(ViewModelKanban):
	_name = "model.kanban.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MKanbanLeOutboundDelivery(ViewModelO2MKanban):
	_name = "model.o2mkanban.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelMdxLeOutboundDelivery(ViewModelMdx):
	_name = "model.mdx.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MMdxLeOutboundDelivery(ViewModelO2MMdx):
	_name = "modelo2mmdx.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MListLeOutboundDelivery(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery"
	_model = "le.outbound.delivery"
	_description = "Outbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts']
