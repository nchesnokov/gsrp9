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

class ViewModelSearchLeInboundDelivery(ViewModelSearch):
	_name = "model.search.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelFindLeInboundDelivery(ViewModelFind):
	_name = "model.find.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelListLeInboundDelivery(ViewModelList):
	_name = "model.list.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts']

class ViewModelFormModalLeInboundDelivery(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelFormLeInboundDelivery(ViewModelForm):
	_name = "model.form.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelO2MFormLeInboundDelivery(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts', 'note']

class ViewModelCalendarLeInboundDelivery(ViewModelCalendar):
	_name = "model.calendar.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MCalendarLeInboundDelivery(ViewModelO2MCalendar):
	_name = "vodel.o2mcalendar.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelGraphLeInboundDelivery(ViewModelGraph):
	_name = "model.graph.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MGraphLeInboundDelivery(ViewModelO2MGraph):
	_name = "model.o2mgraph.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelKanbanLeInboundDelivery(ViewModelKanban):
	_name = "model.kanban.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelO2MKanbanLeInboundDelivery(ViewModelO2MKanban):
	_name = "model.o2mkanban.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'note']

class ViewModelMdxLeInboundDelivery(ViewModelMdx):
	_name = "model.mdx.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MMdxLeInboundDelivery(ViewModelO2MMdx):
	_name = "modelo2mmdx.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount']

class ViewModelO2MListLeInboundDelivery(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery"
	_model = "le.inbound.delivery"
	_description = "Inbound Delivery"
	_columns = ['dtype', 'company_id', 'point_id', 'place_id', 'category_id', 'name', 'origin', 'dod', 'partner', 'currency', 'incoterms1', 'incoterms2', 'state', 'amount', 'vat_amount', 'total_amount', 'items', 'roles', 'texts']
