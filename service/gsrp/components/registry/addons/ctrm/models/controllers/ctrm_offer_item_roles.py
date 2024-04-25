from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmOfferItemRoles(ViewModelFindController):
	_name = "find:ctrm.offer.item.roles"
	_view_name = "ctrm.offer.item.roles/find"
	_description = "CTRM Offer Item Roles"

class ViewModelO2MFormCtrmOfferItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.offer.item.roles"
	_view_name = "ctrm.offer.item.roles/o2m-form"
	_description = "CTRM Offer Item Roles"

class ViewModelO2MListCtrmOfferItemRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.offer.item.roles"
	_view_name = "ctrm.offer.item.roles/o2m-list"
	_description = "CTRM Offer Item Roles"
