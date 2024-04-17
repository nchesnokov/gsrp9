from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsWorkcenterProductPrices(ViewModelFindController):
	_name = "find:ehs.workcenter.product.prices"
	_view_name = "ehs.workcenter.product.prices/find"
	_description = "Workcenter Product Prices"

class ViewModelO2MFormEhsWorkcenterProductPrices(ViewModelO2MFormController):
	_name = "o2m-form:ehs.workcenter.product.prices"
	_view_name = "ehs.workcenter.product.prices/o2m-form"
	_description = "Workcenter Product Prices"

class ViewModelO2MGanttEhsWorkcenterProductPrices(ViewModelO2MGanttController):
	_name = "o2m-gantt:ehs.workcenter.product.prices"
	_view_name = "ehs.workcenter.product.prices/o2m-gantt"
	_description = "Workcenter Product Prices"

class ViewModelO2MScheduleEhsWorkcenterProductPrices(ViewModelO2MScheduleController):
	_name = "o2m-schedule:ehs.workcenter.product.prices"
	_view_name = "ehs.workcenter.product.prices/o2m-schedule"
	_description = "Workcenter Product Prices"

class ViewModelO2MListEhsWorkcenterProductPrices(ViewModelO2MListController):
	_name = "o2m-list:ehs.workcenter.product.prices"
	_view_name = "ehs.workcenter.product.prices/o2m-list"
	_description = "Workcenter Product Prices"
