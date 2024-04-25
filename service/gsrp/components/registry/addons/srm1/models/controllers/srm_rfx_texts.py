from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxTexts(ViewModelFindController):
	_name = "find:srm.rfx.texts"
	_view_name = "srm.rfx.texts/find"
	_description = "SRM RFX Texts"

class ViewModelO2MFormSrmRfxTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.texts"
	_view_name = "srm.rfx.texts/o2m-form"
	_description = "SRM RFX Texts"

class ViewModelO2MListSrmRfxTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.texts"
	_view_name = "srm.rfx.texts/o2m-list"
	_description = "SRM RFX Texts"
