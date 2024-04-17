from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmOfferItemTexts(ViewModelFindController):
	_name = "find:ctrm.offer.item.texts"
	_view_name = "ctrm.offer.item.texts/find"
	_description = "CTRM Offer Item Texts"

class ViewModelO2MFormCtrmOfferItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.offer.item.texts"
	_view_name = "ctrm.offer.item.texts/o2m-form"
	_description = "CTRM Offer Item Texts"

class ViewModelO2MListCtrmOfferItemTexts(ViewModelO2MListController):
	_name = "o2m-list:ctrm.offer.item.texts"
	_view_name = "ctrm.offer.item.texts/o2m-list"
	_description = "CTRM Offer Item Texts"
