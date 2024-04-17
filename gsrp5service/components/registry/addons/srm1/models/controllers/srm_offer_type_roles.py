from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferTypeRoles(ViewModelFindController):
	_name = "find:srm.offer.type.roles"
	_view_name = "srm.offer.type.roles/find"
	_description = "Role SRM Offer Types"

class ViewModelO2MFormSrmOfferTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.type.roles"
	_view_name = "srm.offer.type.roles/o2m-form"
	_description = "Role SRM Offer Types"

class ViewModelO2MListSrmOfferTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.type.roles"
	_view_name = "srm.offer.type.roles/o2m-list"
	_description = "Role SRM Offer Types"
