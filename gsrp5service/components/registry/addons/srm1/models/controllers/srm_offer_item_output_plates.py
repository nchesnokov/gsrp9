from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferItemOutputPlates(ViewModelFindController):
	_name = "find:srm.offer.item.output.plates"
	_view_name = "srm.offer.item.output.plates/find"
	_description = "Offer Item Output Plates"

class ViewModelO2MFormSrmOfferItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.item.output.plates"
	_view_name = "srm.offer.item.output.plates/o2m-form"
	_description = "Offer Item Output Plates"

class ViewModelO2MKanbanSrmOfferItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.offer.item.output.plates"
	_view_name = "srm.offer.item.output.plates/o2m-kanban"
	_description = "Offer Item Output Plates"

class ViewModelO2MListSrmOfferItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.item.output.plates"
	_view_name = "srm.offer.item.output.plates/o2m-list"
	_description = "Offer Item Output Plates"
