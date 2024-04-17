from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmOriginQuotes(ViewModelFindController):
	_name = "find:ctrm.origin.quotes"
	_view_name = "ctrm.origin.quotes/find"
	_description = "Orgigin Quotes of CTRM"

class ViewModelO2MFormCtrmOriginQuotes(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.origin.quotes"
	_view_name = "ctrm.origin.quotes/o2m-form"
	_description = "Orgigin Quotes of CTRM"

class ViewModelO2MListCtrmOriginQuotes(ViewModelO2MListController):
	_name = "o2m-list:ctrm.origin.quotes"
	_view_name = "ctrm.origin.quotes/o2m-list"
	_description = "Orgigin Quotes of CTRM"
