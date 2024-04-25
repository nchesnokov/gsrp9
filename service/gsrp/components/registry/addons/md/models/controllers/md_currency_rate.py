from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdCurrencyRate(ViewModelFindController):
	_name = "find:md.currency.rate"
	_view_name = "md.currency.rate/find"
	_description = "Currency Rate"

class ViewModelO2MFormMdCurrencyRate(ViewModelO2MFormController):
	_name = "o2m-form:md.currency.rate"
	_view_name = "md.currency.rate/o2m-form"
	_description = "Currency Rate"

class ViewModelO2MCalendarMdCurrencyRate(ViewModelO2MCalendarController):
	_name = "o2m-calendar:md.currency.rate"
	_view_name = "md.currency.rate/o2m-calendar"
	_description = "Currency Rate"

class ViewModelO2MGraphMdCurrencyRate(ViewModelO2MGraphController):
	_name = "o2m-graph:md.currency.rate"
	_view_name = "md.currency.rate/o2m-graph"
	_description = "Currency Rate"

class ViewModelO2MMdxMdCurrencyRate(ViewModelO2MMdxController):
	_name = "o2m-mdx:md.currency.rate"
	_view_name = "md.currency.rate/o2m-mdx"
	_description = "Currency Rate"

class ViewModelO2MListMdCurrencyRate(ViewModelO2MListController):
	_name = "o2m-list:md.currency.rate"
	_view_name = "md.currency.rate/o2m-list"
	_description = "Currency Rate"
