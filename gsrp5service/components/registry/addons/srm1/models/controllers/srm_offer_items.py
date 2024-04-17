from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferItems(ViewModelFindController):
	_name = "find:srm.offer.items"
	_view_name = "srm.offer.items/find"
	_description = "SRM Offer Item"

class ViewModelO2MFormSrmOfferItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.items"
	_view_name = "srm.offer.items/o2m-form"
	_description = "SRM Offer Item"

class ViewModelO2MListSrmOfferItems(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.items"
	_view_name = "srm.offer.items/o2m-list"
	_description = "SRM Offer Item"
