from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxItems(ViewModelFindController):
	_name = "find:srm.rfx.items"
	_view_name = "srm.rfx.items/find"
	_description = "SRM RFX Item"

class ViewModelO2MFormSrmRfxItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.items"
	_view_name = "srm.rfx.items/o2m-form"
	_description = "SRM RFX Item"

class ViewModelO2MListSrmRfxItems(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.items"
	_view_name = "srm.rfx.items/o2m-list"
	_description = "SRM RFX Item"
