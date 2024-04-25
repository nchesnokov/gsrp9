from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOfferItemTexts(ViewModelFindController):
	_name = "find:crm.offer.item.texts"
	_view_name = "crm.offer.item.texts/find"
	_description = "CRM Offer Item Texts"

class ViewModelO2MFormCrmOfferItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.offer.item.texts"
	_view_name = "crm.offer.item.texts/o2m-form"
	_description = "CRM Offer Item Texts"

class ViewModelO2MListCrmOfferItemTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.offer.item.texts"
	_view_name = "crm.offer.item.texts/o2m-list"
	_description = "CRM Offer Item Texts"
