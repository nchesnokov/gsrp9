from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferRoles(ViewModelFindController):
	_name = "find:srm.offer.roles"
	_view_name = "srm.offer.roles/find"
	_description = "SRM Offer Roles"

class ViewModelO2MFormSrmOfferRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.roles"
	_view_name = "srm.offer.roles/o2m-form"
	_description = "SRM Offer Roles"

class ViewModelO2MListSrmOfferRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.roles"
	_view_name = "srm.offer.roles/o2m-list"
	_description = "SRM Offer Roles"
