from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdPartnerAddresses(ViewModelFindController):
	_name = "find:md.partner.addresses"
	_view_name = "md.partner.addresses/find"
	_description = "Partner Addresses"

class ViewModelO2MFormMdPartnerAddresses(ViewModelO2MFormController):
	_name = "o2m-form:md.partner.addresses"
	_view_name = "md.partner.addresses/o2m-form"
	_description = "Partner Addresses"

class ViewModelO2MListMdPartnerAddresses(ViewModelO2MListController):
	_name = "o2m-list:md.partner.addresses"
	_view_name = "md.partner.addresses/o2m-list"
	_description = "Partner Addresses"
