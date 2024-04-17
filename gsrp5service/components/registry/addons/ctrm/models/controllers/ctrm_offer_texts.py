from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmOfferTexts(ViewModelFindController):
	_name = "find:ctrm.offer.texts"
	_view_name = "ctrm.offer.texts/find"
	_description = "CTRM Offer Texts"

class ViewModelO2MFormCtrmOfferTexts(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.offer.texts"
	_view_name = "ctrm.offer.texts/o2m-form"
	_description = "CTRM Offer Texts"

class ViewModelO2MListCtrmOfferTexts(ViewModelO2MListController):
	_name = "o2m-list:ctrm.offer.texts"
	_view_name = "ctrm.offer.texts/o2m-list"
	_description = "CTRM Offer Texts"
