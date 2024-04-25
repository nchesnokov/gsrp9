from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdBomItems(ViewModelFindController):
	_name = "find:md.bom.items"
	_view_name = "md.bom.items/find"
	_description = "BoM items"

class ViewModelO2MFormMdBomItems(ViewModelO2MFormController):
	_name = "o2m-form:md.bom.items"
	_view_name = "md.bom.items/o2m-form"
	_description = "BoM items"

class ViewModelO2MListMdBomItems(ViewModelO2MListController):
	_name = "o2m-list:md.bom.items"
	_view_name = "md.bom.items/o2m-list"
	_description = "BoM items"
