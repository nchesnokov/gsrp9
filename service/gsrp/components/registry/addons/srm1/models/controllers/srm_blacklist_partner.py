from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmBlacklistPartner(ViewModelSearchController):
	_name = "search:srm.blacklist.partner"
	_view_name = "srm.blacklist.partner/search"
	_description = "SRM Partner Blacklist"

class ViewModelFindSrmBlacklistPartner(ViewModelFindController):
	_name = "find:srm.blacklist.partner"
	_view_name = "srm.blacklist.partner/find"
	_description = "SRM Partner Blacklist"

class ViewModelListSrmBlacklistPartner(ViewModelListController):
	_name = "list:srm.blacklist.partner"
	_view_name = "srm.blacklist.partner/list"
	_description = "SRM Partner Blacklist"

class ViewModelFormModalSrmBlacklistPartner(ViewModelFormModalController):
	_name = "form.modal:srm.blacklist.partner"
	_view_name = "srm.blacklist.partner/form.modal"
	_description = "SRM Partner Blacklist"

class ViewModelFormSrmBlacklistPartner(ViewModelFormController):
	_name = "form:srm.blacklist.partner"
	_view_name = "srm.blacklist.partner/form"
	_description = "SRM Partner Blacklist"
