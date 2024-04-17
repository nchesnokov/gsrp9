from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOfferRoles(ViewModelFindController):
	_name = "find:crm.offer.roles"
	_view_name = "crm.offer.roles/find"
	_description = "CRM Offer Roles"

class ViewModelO2MFormCrmOfferRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.offer.roles"
	_view_name = "crm.offer.roles/o2m-form"
	_description = "CRM Offer Roles"

class ViewModelO2MListCrmOfferRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.offer.roles"
	_view_name = "crm.offer.roles/o2m-list"
	_description = "CRM Offer Roles"
