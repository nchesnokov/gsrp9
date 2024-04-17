from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxRoles(ViewModelFindController):
	_name = "find:srm.rfx.roles"
	_view_name = "srm.rfx.roles/find"
	_description = "SRM RFX Roles"

class ViewModelO2MFormSrmRfxRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.roles"
	_view_name = "srm.rfx.roles/o2m-form"
	_description = "SRM RFX Roles"

class ViewModelO2MListSrmRfxRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.roles"
	_view_name = "srm.rfx.roles/o2m-list"
	_description = "SRM RFX Roles"
