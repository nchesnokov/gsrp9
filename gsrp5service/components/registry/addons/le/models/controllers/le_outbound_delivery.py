from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchLeOutboundDelivery(ViewModelSearchController):
	_name = "search:le.outbound.delivery"
	_view_name = "le.outbound.delivery/search"
	_description = "Outbound Delivery"

class ViewModelFindLeOutboundDelivery(ViewModelFindController):
	_name = "find:le.outbound.delivery"
	_view_name = "le.outbound.delivery/find"
	_description = "Outbound Delivery"

class ViewModelListLeOutboundDelivery(ViewModelListController):
	_name = "list:le.outbound.delivery"
	_view_name = "le.outbound.delivery/list"
	_description = "Outbound Delivery"

class ViewModelFormModalLeOutboundDelivery(ViewModelFormModalController):
	_name = "form.modal:le.outbound.delivery"
	_view_name = "le.outbound.delivery/form.modal"
	_description = "Outbound Delivery"

class ViewModelFormLeOutboundDelivery(ViewModelFormController):
	_name = "form:le.outbound.delivery"
	_view_name = "le.outbound.delivery/form"
	_description = "Outbound Delivery"

class ViewModelCalendarLeOutboundDelivery(ViewModelCalendarController):
	_name = "calendar:le.outbound.delivery"
	_view_name = "le.outbound.delivery/calendar"
	_description = "Outbound Delivery"

class ViewModelGraphLeOutboundDelivery(ViewModelGraphController):
	_name = "graph:le.outbound.delivery"
	_view_name = "le.outbound.delivery/graph"
	_description = "Outbound Delivery"

class ViewModelKanbanLeOutboundDelivery(ViewModelKanbanController):
	_name = "kanban:le.outbound.delivery"
	_view_name = "le.outbound.delivery/kanban"
	_description = "Outbound Delivery"

class ViewModelMdxLeOutboundDelivery(ViewModelMdxController):
	_name = "mdx:le.outbound.delivery"
	_view_name = "le.outbound.delivery/mdx"
	_description = "Outbound Delivery"
