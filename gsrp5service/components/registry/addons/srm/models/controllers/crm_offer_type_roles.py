from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOfferTypeRoles(ViewModelFindController):
	_name = "find:crm.offer.type.roles"
	_view_name = "crm.offer.type.roles/find"
	_description = "Role CRM Offer Types"

class ViewModelO2MFormCrmOfferTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.offer.type.roles"
	_view_name = "crm.offer.type.roles/o2m-form"
	_description = "Role CRM Offer Types"

class ViewModelO2MListCrmOfferTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.offer.type.roles"
	_view_name = "crm.offer.type.roles/o2m-list"
	_description = "Role CRM Offer Types"
