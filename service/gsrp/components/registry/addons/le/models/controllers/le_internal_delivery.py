from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchLeInternalDelivery(ViewModelSearchController):
	_name = "search:le.internal.delivery"
	_view_name = "le.internal.delivery/search"
	_description = "Internal Delivery"

class ViewModelFindLeInternalDelivery(ViewModelFindController):
	_name = "find:le.internal.delivery"
	_view_name = "le.internal.delivery/find"
	_description = "Internal Delivery"

class ViewModelListLeInternalDelivery(ViewModelListController):
	_name = "list:le.internal.delivery"
	_view_name = "le.internal.delivery/list"
	_description = "Internal Delivery"

class ViewModelFormModalLeInternalDelivery(ViewModelFormModalController):
	_name = "form.modal:le.internal.delivery"
	_view_name = "le.internal.delivery/form.modal"
	_description = "Internal Delivery"

class ViewModelFormLeInternalDelivery(ViewModelFormController):
	_name = "form:le.internal.delivery"
	_view_name = "le.internal.delivery/form"
	_description = "Internal Delivery"

class ViewModelCalendarLeInternalDelivery(ViewModelCalendarController):
	_name = "calendar:le.internal.delivery"
	_view_name = "le.internal.delivery/calendar"
	_description = "Internal Delivery"

class ViewModelGraphLeInternalDelivery(ViewModelGraphController):
	_name = "graph:le.internal.delivery"
	_view_name = "le.internal.delivery/graph"
	_description = "Internal Delivery"

class ViewModelKanbanLeInternalDelivery(ViewModelKanbanController):
	_name = "kanban:le.internal.delivery"
	_view_name = "le.internal.delivery/kanban"
	_description = "Internal Delivery"

class ViewModelMdxLeInternalDelivery(ViewModelMdxController):
	_name = "mdx:le.internal.delivery"
	_view_name = "le.internal.delivery/mdx"
	_description = "Internal Delivery"
