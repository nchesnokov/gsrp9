from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmOfferTypes(ViewModelSearchController):
	_name = "search:srm.offer.types"
	_view_name = "srm.offer.types/search"
	_description = "Types SRM Offer"

class ViewModelFindSrmOfferTypes(ViewModelFindController):
	_name = "find:srm.offer.types"
	_view_name = "srm.offer.types/find"
	_description = "Types SRM Offer"

class ViewModelListSrmOfferTypes(ViewModelListController):
	_name = "list:srm.offer.types"
	_view_name = "srm.offer.types/list"
	_description = "Types SRM Offer"

class ViewModelFormModalSrmOfferTypes(ViewModelFormModalController):
	_name = "form.modal:srm.offer.types"
	_view_name = "srm.offer.types/form.modal"
	_description = "Types SRM Offer"

class ViewModelFormSrmOfferTypes(ViewModelFormController):
	_name = "form:srm.offer.types"
	_view_name = "srm.offer.types/form"
	_description = "Types SRM Offer"
