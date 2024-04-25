from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferTypeDeadlines(ViewModelFindController):
	_name = "find:srm.offer.type.deadlines"
	_view_name = "srm.offer.type.deadlines/find"
	_description = "Deadlines SRM Offer Types"

class ViewModelO2MFormSrmOfferTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.type.deadlines"
	_view_name = "srm.offer.type.deadlines/o2m-form"
	_description = "Deadlines SRM Offer Types"

class ViewModelO2MListSrmOfferTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.type.deadlines"
	_view_name = "srm.offer.type.deadlines/o2m-list"
	_description = "Deadlines SRM Offer Types"
