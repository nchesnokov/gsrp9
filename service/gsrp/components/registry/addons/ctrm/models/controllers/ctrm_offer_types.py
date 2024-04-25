from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmOfferTypes(ViewModelSearchController):
	_name = "search:ctrm.offer.types"
	_view_name = "ctrm.offer.types/search"
	_description = "Types CTRM Offer"

class ViewModelFindCtrmOfferTypes(ViewModelFindController):
	_name = "find:ctrm.offer.types"
	_view_name = "ctrm.offer.types/find"
	_description = "Types CTRM Offer"

class ViewModelListCtrmOfferTypes(ViewModelListController):
	_name = "list:ctrm.offer.types"
	_view_name = "ctrm.offer.types/list"
	_description = "Types CTRM Offer"

class ViewModelFormModalCtrmOfferTypes(ViewModelFormModalController):
	_name = "form.modal:ctrm.offer.types"
	_view_name = "ctrm.offer.types/form.modal"
	_description = "Types CTRM Offer"

class ViewModelFormCtrmOfferTypes(ViewModelFormController):
	_name = "form:ctrm.offer.types"
	_view_name = "ctrm.offer.types/form"
	_description = "Types CTRM Offer"
