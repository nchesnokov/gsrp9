from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferTexts(ViewModelFindController):
	_name = "find:srm.offer.texts"
	_view_name = "srm.offer.texts/find"
	_description = "SRM Offer Texts"

class ViewModelO2MFormSrmOfferTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.texts"
	_view_name = "srm.offer.texts/o2m-form"
	_description = "SRM Offer Texts"

class ViewModelO2MListSrmOfferTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.texts"
	_view_name = "srm.offer.texts/o2m-list"
	_description = "SRM Offer Texts"
