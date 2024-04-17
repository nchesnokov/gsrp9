from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferOutputPlates(ViewModelFindController):
	_name = "find:srm.offer.output.plates"
	_view_name = "srm.offer.output.plates/find"
	_description = "SRM Offer Output Plates"

class ViewModelO2MFormSrmOfferOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.output.plates"
	_view_name = "srm.offer.output.plates/o2m-form"
	_description = "SRM Offer Output Plates"

class ViewModelO2MKanbanSrmOfferOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.offer.output.plates"
	_view_name = "srm.offer.output.plates/o2m-kanban"
	_description = "SRM Offer Output Plates"

class ViewModelO2MListSrmOfferOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.output.plates"
	_view_name = "srm.offer.output.plates/o2m-list"
	_description = "SRM Offer Output Plates"
