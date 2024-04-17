from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmOfferTypeRoles(ViewModelFindController):
	_name = "find:ctrm.offer.type.roles"
	_view_name = "ctrm.offer.type.roles/find"
	_description = "Role CTRM Offer Types"

class ViewModelO2MFormCtrmOfferTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.offer.type.roles"
	_view_name = "ctrm.offer.type.roles/o2m-form"
	_description = "Role CTRM Offer Types"

class ViewModelO2MListCtrmOfferTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.offer.type.roles"
	_view_name = "ctrm.offer.type.roles/o2m-list"
	_description = "Role CTRM Offer Types"
