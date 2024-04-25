from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGeoController

class ViewModelSearchMdPartner(ViewModelSearchController):
	_name = "search:md.partner"
	_view_name = "md.partner/search"
	_description = "Partner"

class ViewModelFindMdPartner(ViewModelFindController):
	_name = "find:md.partner"
	_view_name = "md.partner/find"
	_description = "Partner"

class ViewModelListMdPartner(ViewModelListController):
	_name = "list:md.partner"
	_view_name = "md.partner/list"
	_description = "Partner"

class ViewModelFormModalMdPartner(ViewModelFormModalController):
	_name = "form.modal:md.partner"
	_view_name = "md.partner/form.modal"
	_description = "Partner"

class ViewModelFormMdPartner(ViewModelFormController):
	_name = "form:md.partner"
	_view_name = "md.partner/form"
	_description = "Partner"

class ViewModelGeoMdPartner(ViewModelGeoController):
	_name = "geo:md.partner"
	_view_name = "md.partner/geo"
	_description = "Partner"
