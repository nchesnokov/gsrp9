from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpRequestItems(ViewModelFindController):
	_name = "find:mrp.request.items"
	_view_name = "mrp.request.items/find"
	_description = "MRP Request Item"

class ViewModelO2MFormMrpRequestItems(ViewModelO2MFormController):
	_name = "o2m-form:mrp.request.items"
	_view_name = "mrp.request.items/o2m-form"
	_description = "MRP Request Item"

class ViewModelO2MListMrpRequestItems(ViewModelO2MListController):
	_name = "o2m-list:mrp.request.items"
	_view_name = "mrp.request.items/o2m-list"
	_description = "MRP Request Item"
