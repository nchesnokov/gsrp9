from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCmCostOrderDates(ViewModelFindController):
	_name = "find:cm.cost.order.dates"
	_view_name = "cm.cost.order.dates/find"
	_description = "Cost Order Dates"

class ViewModelO2MFormCmCostOrderDates(ViewModelO2MFormController):
	_name = "o2m-form:cm.cost.order.dates"
	_view_name = "cm.cost.order.dates/o2m-form"
	_description = "Cost Order Dates"

class ViewModelO2MCalendarCmCostOrderDates(ViewModelO2MCalendarController):
	_name = "o2m-calendar:cm.cost.order.dates"
	_view_name = "cm.cost.order.dates/o2m-calendar"
	_description = "Cost Order Dates"

class ViewModelO2MGraphCmCostOrderDates(ViewModelO2MGraphController):
	_name = "o2m-graph:cm.cost.order.dates"
	_view_name = "cm.cost.order.dates/o2m-graph"
	_description = "Cost Order Dates"

class ViewModelO2MMdxCmCostOrderDates(ViewModelO2MMdxController):
	_name = "o2m-mdx:cm.cost.order.dates"
	_view_name = "cm.cost.order.dates/o2m-mdx"
	_description = "Cost Order Dates"

class ViewModelO2MListCmCostOrderDates(ViewModelO2MListController):
	_name = "o2m-list:cm.cost.order.dates"
	_view_name = "cm.cost.order.dates/o2m-list"
	_description = "Cost Order Dates"
