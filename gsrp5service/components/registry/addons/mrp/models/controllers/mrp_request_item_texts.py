from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpRequestItemTexts(ViewModelFindController):
	_name = "find:mrp.request.item.texts"
	_view_name = "mrp.request.item.texts/find"
	_description = "MRP Request Item Texts"

class ViewModelO2MFormMrpRequestItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:mrp.request.item.texts"
	_view_name = "mrp.request.item.texts/o2m-form"
	_description = "MRP Request Item Texts"

class ViewModelO2MListMrpRequestItemTexts(ViewModelO2MListController):
	_name = "o2m-list:mrp.request.item.texts"
	_view_name = "mrp.request.item.texts/o2m-list"
	_description = "MRP Request Item Texts"
