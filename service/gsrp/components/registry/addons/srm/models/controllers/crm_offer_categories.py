from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmOfferCategories(ViewModelSearchController):
	_name = "search:crm.offer.categories"
	_view_name = "crm.offer.categories/search"
	_description = "Category CRM Offer"

class ViewModelFindCrmOfferCategories(ViewModelFindController):
	_name = "find:crm.offer.categories"
	_view_name = "crm.offer.categories/find"
	_description = "Category CRM Offer"

class ViewModelListCrmOfferCategories(ViewModelListController):
	_name = "list:crm.offer.categories"
	_view_name = "crm.offer.categories/list"
	_description = "Category CRM Offer"

class ViewModelFormModalCrmOfferCategories(ViewModelFormModalController):
	_name = "form.modal:crm.offer.categories"
	_view_name = "crm.offer.categories/form.modal"
	_description = "Category CRM Offer"

class ViewModelFormCrmOfferCategories(ViewModelFormController):
	_name = "form:crm.offer.categories"
	_view_name = "crm.offer.categories/form"
	_description = "Category CRM Offer"

class ViewModelTreeCrmOfferCategories(ViewModelTreeController):
	_name = "tree:crm.offer.categories"
	_view_name = "crm.offer.categories/tree"
	_description = "Category CRM Offer"
