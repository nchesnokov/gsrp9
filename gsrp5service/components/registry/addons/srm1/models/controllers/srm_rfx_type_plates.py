from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxTypePlates(ViewModelFindController):
	_name = "find:srm.rfx.type.plates"
	_view_name = "srm.rfx.type.plates/find"
	_description = "SRM RFX Plates"

class ViewModelO2MFormSrmRfxTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.type.plates"
	_view_name = "srm.rfx.type.plates/o2m-form"
	_description = "SRM RFX Plates"

class ViewModelO2MListSrmRfxTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.type.plates"
	_view_name = "srm.rfx.type.plates/o2m-list"
	_description = "SRM RFX Plates"
