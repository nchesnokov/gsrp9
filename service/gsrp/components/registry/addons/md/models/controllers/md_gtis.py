from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdGtis(ViewModelSearchController):
	_name = "search:md.gtis"
	_view_name = "md.gtis/search"
	_description = "Group Of Type Items"

class ViewModelFindMdGtis(ViewModelFindController):
	_name = "find:md.gtis"
	_view_name = "md.gtis/find"
	_description = "Group Of Type Items"

class ViewModelListMdGtis(ViewModelListController):
	_name = "list:md.gtis"
	_view_name = "md.gtis/list"
	_description = "Group Of Type Items"

class ViewModelFormModalMdGtis(ViewModelFormModalController):
	_name = "form.modal:md.gtis"
	_view_name = "md.gtis/form.modal"
	_description = "Group Of Type Items"

class ViewModelFormMdGtis(ViewModelFormController):
	_name = "form:md.gtis"
	_view_name = "md.gtis/form"
	_description = "Group Of Type Items"
