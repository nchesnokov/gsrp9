from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxTypeDeadlines(ViewModelFindController):
	_name = "find:srm.rfx.type.deadlines"
	_view_name = "srm.rfx.type.deadlines/find"
	_description = "Deadlines SRM RFX Types"

class ViewModelO2MFormSrmRfxTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.type.deadlines"
	_view_name = "srm.rfx.type.deadlines/o2m-form"
	_description = "Deadlines SRM RFX Types"

class ViewModelO2MListSrmRfxTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.type.deadlines"
	_view_name = "srm.rfx.type.deadlines/o2m-list"
	_description = "Deadlines SRM RFX Types"
