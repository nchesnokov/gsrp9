from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxTypeItems(ViewModelFindController):
	_name = "find:srm.rfx.type.items"
	_view_name = "srm.rfx.type.items/find"
	_description = "Type of SRM RFX Items"

class ViewModelO2MFormSrmRfxTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.type.items"
	_view_name = "srm.rfx.type.items/o2m-form"
	_description = "Type of SRM RFX Items"

class ViewModelO2MListSrmRfxTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.type.items"
	_view_name = "srm.rfx.type.items/o2m-list"
	_description = "Type of SRM RFX Items"
