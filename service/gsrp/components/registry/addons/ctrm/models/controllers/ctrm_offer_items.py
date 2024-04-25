from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmOfferItems(ViewModelFindController):
	_name = "find:ctrm.offer.items"
	_view_name = "ctrm.offer.items/find"
	_description = "CTRM Offer Items"

class ViewModelO2MFormCtrmOfferItems(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.offer.items"
	_view_name = "ctrm.offer.items/o2m-form"
	_description = "CTRM Offer Items"

class ViewModelO2MListCtrmOfferItems(ViewModelO2MListController):
	_name = "o2m-list:ctrm.offer.items"
	_view_name = "ctrm.offer.items/o2m-list"
	_description = "CTRM Offer Items"
