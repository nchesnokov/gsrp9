from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchCrmOffers(ViewModelSearchController):
	_name = "search:crm.offers"
	_view_name = "crm.offers/search"
	_description = "CRM Offers"

class ViewModelFindCrmOffers(ViewModelFindController):
	_name = "find:crm.offers"
	_view_name = "crm.offers/find"
	_description = "CRM Offers"

class ViewModelListCrmOffers(ViewModelListController):
	_name = "list:crm.offers"
	_view_name = "crm.offers/list"
	_description = "CRM Offers"

class ViewModelFormModalCrmOffers(ViewModelFormModalController):
	_name = "form.modal:crm.offers"
	_view_name = "crm.offers/form.modal"
	_description = "CRM Offers"

class ViewModelFormCrmOffers(ViewModelFormController):
	_name = "form:crm.offers"
	_view_name = "crm.offers/form"
	_description = "CRM Offers"

class ViewModelCalendarCrmOffers(ViewModelCalendarController):
	_name = "calendar:crm.offers"
	_view_name = "crm.offers/calendar"
	_description = "CRM Offers"

class ViewModelGraphCrmOffers(ViewModelGraphController):
	_name = "graph:crm.offers"
	_view_name = "crm.offers/graph"
	_description = "CRM Offers"

class ViewModelMdxCrmOffers(ViewModelMdxController):
	_name = "mdx:crm.offers"
	_view_name = "crm.offers/mdx"
	_description = "CRM Offers"
