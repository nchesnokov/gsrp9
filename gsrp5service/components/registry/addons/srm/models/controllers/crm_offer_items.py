from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOfferItems(ViewModelFindController):
	_name = "find:crm.offer.items"
	_view_name = "crm.offer.items/find"
	_description = "CRM Offer Items"

class ViewModelO2MFormCrmOfferItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.offer.items"
	_view_name = "crm.offer.items/o2m-form"
	_description = "CRM Offer Items"

class ViewModelO2MListCrmOfferItems(ViewModelO2MListController):
	_name = "o2m-list:crm.offer.items"
	_view_name = "crm.offer.items/o2m-list"
	_description = "CRM Offer Items"
