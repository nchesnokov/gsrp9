from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmWorkcenterProductPrices(ViewModelFindController):
	_name = "find:mm.workcenter.product.prices"
	_view_name = "mm.workcenter.product.prices/find"
	_description = "Workcenter Product Prices"

class ViewModelO2MFormMmWorkcenterProductPrices(ViewModelO2MFormController):
	_name = "o2m-form:mm.workcenter.product.prices"
	_view_name = "mm.workcenter.product.prices/o2m-form"
	_description = "Workcenter Product Prices"

class ViewModelO2MGanttMmWorkcenterProductPrices(ViewModelO2MGanttController):
	_name = "o2m-gantt:mm.workcenter.product.prices"
	_view_name = "mm.workcenter.product.prices/o2m-gantt"
	_description = "Workcenter Product Prices"

class ViewModelO2MScheduleMmWorkcenterProductPrices(ViewModelO2MScheduleController):
	_name = "o2m-schedule:mm.workcenter.product.prices"
	_view_name = "mm.workcenter.product.prices/o2m-schedule"
	_description = "Workcenter Product Prices"

class ViewModelO2MListMmWorkcenterProductPrices(ViewModelO2MListController):
	_name = "o2m-list:mm.workcenter.product.prices"
	_view_name = "mm.workcenter.product.prices/o2m-list"
	_description = "Workcenter Product Prices"
