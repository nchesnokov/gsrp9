from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmRequestItems(ViewModelFindController):
	_name = "find:ctrm.request.items"
	_view_name = "ctrm.request.items/find"
	_description = "CTRM Request Items"

class ViewModelO2MFormCtrmRequestItems(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.request.items"
	_view_name = "ctrm.request.items/o2m-form"
	_description = "CTRM Request Items"

class ViewModelO2MListCtrmRequestItems(ViewModelO2MListController):
	_name = "o2m-list:ctrm.request.items"
	_view_name = "ctrm.request.items/o2m-list"
	_description = "CTRM Request Items"
