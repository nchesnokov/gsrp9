from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchLeInboundDelivery(ViewModelSearchController):
	_name = "search:le.inbound.delivery"
	_view_name = "le.inbound.delivery/search"
	_description = "Inbound Delivery"

class ViewModelFindLeInboundDelivery(ViewModelFindController):
	_name = "find:le.inbound.delivery"
	_view_name = "le.inbound.delivery/find"
	_description = "Inbound Delivery"

class ViewModelListLeInboundDelivery(ViewModelListController):
	_name = "list:le.inbound.delivery"
	_view_name = "le.inbound.delivery/list"
	_description = "Inbound Delivery"

class ViewModelFormModalLeInboundDelivery(ViewModelFormModalController):
	_name = "form.modal:le.inbound.delivery"
	_view_name = "le.inbound.delivery/form.modal"
	_description = "Inbound Delivery"

class ViewModelFormLeInboundDelivery(ViewModelFormController):
	_name = "form:le.inbound.delivery"
	_view_name = "le.inbound.delivery/form"
	_description = "Inbound Delivery"

class ViewModelCalendarLeInboundDelivery(ViewModelCalendarController):
	_name = "calendar:le.inbound.delivery"
	_view_name = "le.inbound.delivery/calendar"
	_description = "Inbound Delivery"

class ViewModelGraphLeInboundDelivery(ViewModelGraphController):
	_name = "graph:le.inbound.delivery"
	_view_name = "le.inbound.delivery/graph"
	_description = "Inbound Delivery"

class ViewModelKanbanLeInboundDelivery(ViewModelKanbanController):
	_name = "kanban:le.inbound.delivery"
	_view_name = "le.inbound.delivery/kanban"
	_description = "Inbound Delivery"

class ViewModelMdxLeInboundDelivery(ViewModelMdxController):
	_name = "mdx:le.inbound.delivery"
	_view_name = "le.inbound.delivery/mdx"
	_description = "Inbound Delivery"
