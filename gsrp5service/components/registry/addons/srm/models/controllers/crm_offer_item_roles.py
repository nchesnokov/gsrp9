from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOfferItemRoles(ViewModelFindController):
	_name = "find:crm.offer.item.roles"
	_view_name = "crm.offer.item.roles/find"
	_description = "CRM Offer Item Roles"

class ViewModelO2MFormCrmOfferItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.offer.item.roles"
	_view_name = "crm.offer.item.roles/o2m-form"
	_description = "CRM Offer Item Roles"

class ViewModelO2MListCrmOfferItemRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.offer.item.roles"
	_view_name = "crm.offer.item.roles/o2m-list"
	_description = "CRM Offer Item Roles"
