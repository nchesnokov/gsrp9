from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmOfferRoles(ViewModelFindController):
	_name = "find:ctrm.offer.roles"
	_view_name = "ctrm.offer.roles/find"
	_description = "CTRM Offer Roles"

class ViewModelO2MFormCtrmOfferRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.offer.roles"
	_view_name = "ctrm.offer.roles/o2m-form"
	_description = "CTRM Offer Roles"

class ViewModelO2MListCtrmOfferRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.offer.roles"
	_view_name = "ctrm.offer.roles/o2m-list"
	_description = "CTRM Offer Roles"
