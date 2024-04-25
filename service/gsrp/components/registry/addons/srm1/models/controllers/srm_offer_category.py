from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmOfferCategory(ViewModelSearchController):
	_name = "search:srm.offer.category"
	_view_name = "srm.offer.category/search"
	_description = "Category SRM Offer"

class ViewModelFindSrmOfferCategory(ViewModelFindController):
	_name = "find:srm.offer.category"
	_view_name = "srm.offer.category/find"
	_description = "Category SRM Offer"

class ViewModelListSrmOfferCategory(ViewModelListController):
	_name = "list:srm.offer.category"
	_view_name = "srm.offer.category/list"
	_description = "Category SRM Offer"

class ViewModelFormModalSrmOfferCategory(ViewModelFormModalController):
	_name = "form.modal:srm.offer.category"
	_view_name = "srm.offer.category/form.modal"
	_description = "Category SRM Offer"

class ViewModelFormSrmOfferCategory(ViewModelFormController):
	_name = "form:srm.offer.category"
	_view_name = "srm.offer.category/form"
	_description = "Category SRM Offer"

class ViewModelTreeSrmOfferCategory(ViewModelTreeController):
	_name = "tree:srm.offer.category"
	_view_name = "srm.offer.category/tree"
	_description = "Category SRM Offer"
