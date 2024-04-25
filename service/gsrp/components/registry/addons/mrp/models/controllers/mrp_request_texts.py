from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpRequestTexts(ViewModelFindController):
	_name = "find:mrp.request.texts"
	_view_name = "mrp.request.texts/find"
	_description = "MRP Request Texts"

class ViewModelO2MFormMrpRequestTexts(ViewModelO2MFormController):
	_name = "o2m-form:mrp.request.texts"
	_view_name = "mrp.request.texts/o2m-form"
	_description = "MRP Request Texts"

class ViewModelO2MListMrpRequestTexts(ViewModelO2MListController):
	_name = "o2m-list:mrp.request.texts"
	_view_name = "mrp.request.texts/o2m-list"
	_description = "MRP Request Texts"
