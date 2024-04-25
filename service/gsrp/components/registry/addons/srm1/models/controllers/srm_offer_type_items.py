from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferTypeItems(ViewModelFindController):
	_name = "find:srm.offer.type.items"
	_view_name = "srm.offer.type.items/find"
	_description = "Type of SRM Offer Items"

class ViewModelO2MFormSrmOfferTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.type.items"
	_view_name = "srm.offer.type.items/o2m-form"
	_description = "Type of SRM Offer Items"

class ViewModelO2MListSrmOfferTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.type.items"
	_view_name = "srm.offer.type.items/o2m-list"
	_description = "Type of SRM Offer Items"
