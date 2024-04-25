from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCtrmOfferCategories(ViewModelSearchController):
	_name = "search:ctrm.offer.categories"
	_view_name = "ctrm.offer.categories/search"
	_description = "Category CTRM Offer"

class ViewModelFindCtrmOfferCategories(ViewModelFindController):
	_name = "find:ctrm.offer.categories"
	_view_name = "ctrm.offer.categories/find"
	_description = "Category CTRM Offer"

class ViewModelListCtrmOfferCategories(ViewModelListController):
	_name = "list:ctrm.offer.categories"
	_view_name = "ctrm.offer.categories/list"
	_description = "Category CTRM Offer"

class ViewModelFormModalCtrmOfferCategories(ViewModelFormModalController):
	_name = "form.modal:ctrm.offer.categories"
	_view_name = "ctrm.offer.categories/form.modal"
	_description = "Category CTRM Offer"

class ViewModelFormCtrmOfferCategories(ViewModelFormController):
	_name = "form:ctrm.offer.categories"
	_view_name = "ctrm.offer.categories/form"
	_description = "Category CTRM Offer"

class ViewModelTreeCtrmOfferCategories(ViewModelTreeController):
	_name = "tree:ctrm.offer.categories"
	_view_name = "ctrm.offer.categories/tree"
	_description = "Category CTRM Offer"
