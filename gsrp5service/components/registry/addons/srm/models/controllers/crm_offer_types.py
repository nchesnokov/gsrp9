from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmOfferTypes(ViewModelSearchController):
	_name = "search:crm.offer.types"
	_view_name = "crm.offer.types/search"
	_description = "Types CRM Offer"

class ViewModelFindCrmOfferTypes(ViewModelFindController):
	_name = "find:crm.offer.types"
	_view_name = "crm.offer.types/find"
	_description = "Types CRM Offer"

class ViewModelListCrmOfferTypes(ViewModelListController):
	_name = "list:crm.offer.types"
	_view_name = "crm.offer.types/list"
	_description = "Types CRM Offer"

class ViewModelFormModalCrmOfferTypes(ViewModelFormModalController):
	_name = "form.modal:crm.offer.types"
	_view_name = "crm.offer.types/form.modal"
	_description = "Types CRM Offer"

class ViewModelFormCrmOfferTypes(ViewModelFormController):
	_name = "form:crm.offer.types"
	_view_name = "crm.offer.types/form"
	_description = "Types CRM Offer"
