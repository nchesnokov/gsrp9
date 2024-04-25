from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferItemRoles(ViewModelFindController):
	_name = "find:srm.offer.item.roles"
	_view_name = "srm.offer.item.roles/find"
	_description = "SRM Offer Roles"

class ViewModelO2MFormSrmOfferItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.item.roles"
	_view_name = "srm.offer.item.roles/o2m-form"
	_description = "SRM Offer Roles"

class ViewModelO2MListSrmOfferItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.item.roles"
	_view_name = "srm.offer.item.roles/o2m-list"
	_description = "SRM Offer Roles"
