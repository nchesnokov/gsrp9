from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCmCostCenterDates(ViewModelFindController):
	_name = "find:cm.cost.center.dates"
	_view_name = "cm.cost.center.dates/find"
	_description = "Cost Center Dates"

class ViewModelO2MFormCmCostCenterDates(ViewModelO2MFormController):
	_name = "o2m-form:cm.cost.center.dates"
	_view_name = "cm.cost.center.dates/o2m-form"
	_description = "Cost Center Dates"

class ViewModelO2MCalendarCmCostCenterDates(ViewModelO2MCalendarController):
	_name = "o2m-calendar:cm.cost.center.dates"
	_view_name = "cm.cost.center.dates/o2m-calendar"
	_description = "Cost Center Dates"

class ViewModelO2MGraphCmCostCenterDates(ViewModelO2MGraphController):
	_name = "o2m-graph:cm.cost.center.dates"
	_view_name = "cm.cost.center.dates/o2m-graph"
	_description = "Cost Center Dates"

class ViewModelO2MMdxCmCostCenterDates(ViewModelO2MMdxController):
	_name = "o2m-mdx:cm.cost.center.dates"
	_view_name = "cm.cost.center.dates/o2m-mdx"
	_description = "Cost Center Dates"

class ViewModelO2MListCmCostCenterDates(ViewModelO2MListController):
	_name = "o2m-list:cm.cost.center.dates"
	_view_name = "cm.cost.center.dates/o2m-list"
	_description = "Cost Center Dates"
