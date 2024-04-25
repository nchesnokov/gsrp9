from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxItemRoles(ViewModelFindController):
	_name = "find:srm.rfx.item.roles"
	_view_name = "srm.rfx.item.roles/find"
	_description = "SRM RFX Roles"

class ViewModelO2MFormSrmRfxItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.item.roles"
	_view_name = "srm.rfx.item.roles/o2m-form"
	_description = "SRM RFX Roles"

class ViewModelO2MListSrmRfxItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.item.roles"
	_view_name = "srm.rfx.item.roles/o2m-list"
	_description = "SRM RFX Roles"
