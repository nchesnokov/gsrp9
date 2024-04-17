from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderSchedules(ViewModelFindController):
	_name = "find:mm.production.order.schedules"
	_view_name = "mm.production.order.schedules/find"
	_description = "Production Order Schedule"

class ViewModelO2MFormMmProductionOrderSchedules(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.schedules"
	_view_name = "mm.production.order.schedules/o2m-form"
	_description = "Production Order Schedule"

class ViewModelO2MListMmProductionOrderSchedules(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.schedules"
	_view_name = "mm.production.order.schedules/o2m-list"
	_description = "Production Order Schedule"
