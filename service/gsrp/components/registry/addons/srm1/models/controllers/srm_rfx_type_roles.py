from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxTypeRoles(ViewModelFindController):
	_name = "find:srm.rfx.type.roles"
	_view_name = "srm.rfx.type.roles/find"
	_description = "Role SRM RFX Types"

class ViewModelO2MFormSrmRfxTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.type.roles"
	_view_name = "srm.rfx.type.roles/o2m-form"
	_description = "Role SRM RFX Types"

class ViewModelO2MListSrmRfxTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.type.roles"
	_view_name = "srm.rfx.type.roles/o2m-list"
	_description = "Role SRM RFX Types"
