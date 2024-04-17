from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferTypePlates(ViewModelFindController):
	_name = "find:srm.offer.type.plates"
	_view_name = "srm.offer.type.plates/find"
	_description = "SRM Offer Plates"

class ViewModelO2MFormSrmOfferTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.type.plates"
	_view_name = "srm.offer.type.plates/o2m-form"
	_description = "SRM Offer Plates"

class ViewModelO2MListSrmOfferTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.type.plates"
	_view_name = "srm.offer.type.plates/o2m-list"
	_description = "SRM Offer Plates"
