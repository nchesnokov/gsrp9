from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdPartnerRoles(ViewModelFindController):
	_name = "find:md.partner.roles"
	_view_name = "md.partner.roles/find"
	_description = "Partner Roles"

class ViewModelO2MFormMdPartnerRoles(ViewModelO2MFormController):
	_name = "o2m-form:md.partner.roles"
	_view_name = "md.partner.roles/o2m-form"
	_description = "Partner Roles"

class ViewModelO2MListMdPartnerRoles(ViewModelO2MListController):
	_name = "o2m-list:md.partner.roles"
	_view_name = "md.partner.roles/o2m-list"
	_description = "Partner Roles"
