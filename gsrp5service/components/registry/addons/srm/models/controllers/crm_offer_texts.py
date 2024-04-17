from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOfferTexts(ViewModelFindController):
	_name = "find:crm.offer.texts"
	_view_name = "crm.offer.texts/find"
	_description = "CRM Offer Texts"

class ViewModelO2MFormCrmOfferTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.offer.texts"
	_view_name = "crm.offer.texts/o2m-form"
	_description = "CRM Offer Texts"

class ViewModelO2MListCrmOfferTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.offer.texts"
	_view_name = "crm.offer.texts/o2m-list"
	_description = "CRM Offer Texts"
