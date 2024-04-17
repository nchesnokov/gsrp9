from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferItemTexts(ViewModelFindController):
	_name = "find:srm.offer.item.texts"
	_view_name = "srm.offer.item.texts/find"
	_description = "SRM Offer Item Texts"

class ViewModelO2MFormSrmOfferItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.item.texts"
	_view_name = "srm.offer.item.texts/o2m-form"
	_description = "SRM Offer Item Texts"

class ViewModelO2MListSrmOfferItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.item.texts"
	_view_name = "srm.offer.item.texts/o2m-list"
	_description = "SRM Offer Item Texts"
