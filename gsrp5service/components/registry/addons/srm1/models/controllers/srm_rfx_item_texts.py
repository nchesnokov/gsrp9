from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxItemTexts(ViewModelFindController):
	_name = "find:srm.rfx.item.texts"
	_view_name = "srm.rfx.item.texts/find"
	_description = "SRM RFX Item Texts"

class ViewModelO2MFormSrmRfxItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.item.texts"
	_view_name = "srm.rfx.item.texts/o2m-form"
	_description = "SRM RFX Item Texts"

class ViewModelO2MListSrmRfxItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.item.texts"
	_view_name = "srm.rfx.item.texts/o2m-list"
	_description = "SRM RFX Item Texts"
