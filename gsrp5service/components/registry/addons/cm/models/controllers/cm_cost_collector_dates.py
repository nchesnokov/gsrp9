from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCmCostCollectorDates(ViewModelFindController):
	_name = "find:cm.cost.collector.dates"
	_view_name = "cm.cost.collector.dates/find"
	_description = "Cost Collector Dates"

class ViewModelO2MFormCmCostCollectorDates(ViewModelO2MFormController):
	_name = "o2m-form:cm.cost.collector.dates"
	_view_name = "cm.cost.collector.dates/o2m-form"
	_description = "Cost Collector Dates"

class ViewModelO2MCalendarCmCostCollectorDates(ViewModelO2MCalendarController):
	_name = "o2m-calendar:cm.cost.collector.dates"
	_view_name = "cm.cost.collector.dates/o2m-calendar"
	_description = "Cost Collector Dates"

class ViewModelO2MGraphCmCostCollectorDates(ViewModelO2MGraphController):
	_name = "o2m-graph:cm.cost.collector.dates"
	_view_name = "cm.cost.collector.dates/o2m-graph"
	_description = "Cost Collector Dates"

class ViewModelO2MMdxCmCostCollectorDates(ViewModelO2MMdxController):
	_name = "o2m-mdx:cm.cost.collector.dates"
	_view_name = "cm.cost.collector.dates/o2m-mdx"
	_description = "Cost Collector Dates"

class ViewModelO2MListCmCostCollectorDates(ViewModelO2MListController):
	_name = "o2m-list:cm.cost.collector.dates"
	_view_name = "cm.cost.collector.dates/o2m-list"
	_description = "Cost Collector Dates"
