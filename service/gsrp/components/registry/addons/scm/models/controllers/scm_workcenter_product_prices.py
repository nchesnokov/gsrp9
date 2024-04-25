from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmWorkcenterProductPrices(ViewModelFindController):
	_name = "find:scm.workcenter.product.prices"
	_view_name = "scm.workcenter.product.prices/find"
	_description = "Workcenter Product Prices"

class ViewModelO2MFormScmWorkcenterProductPrices(ViewModelO2MFormController):
	_name = "o2m-form:scm.workcenter.product.prices"
	_view_name = "scm.workcenter.product.prices/o2m-form"
	_description = "Workcenter Product Prices"

class ViewModelO2MGanttScmWorkcenterProductPrices(ViewModelO2MGanttController):
	_name = "o2m-gantt:scm.workcenter.product.prices"
	_view_name = "scm.workcenter.product.prices/o2m-gantt"
	_description = "Workcenter Product Prices"

class ViewModelO2MScheduleScmWorkcenterProductPrices(ViewModelO2MScheduleController):
	_name = "o2m-schedule:scm.workcenter.product.prices"
	_view_name = "scm.workcenter.product.prices/o2m-schedule"
	_description = "Workcenter Product Prices"

class ViewModelO2MListScmWorkcenterProductPrices(ViewModelO2MListController):
	_name = "o2m-list:scm.workcenter.product.prices"
	_view_name = "scm.workcenter.product.prices/o2m-list"
	_description = "Workcenter Product Prices"
