from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdBanks(ViewModelSearchController):
	_name = "search:md.banks"
	_view_name = "md.banks/search"
	_description = "Bank"

class ViewModelFindMdBanks(ViewModelFindController):
	_name = "find:md.banks"
	_view_name = "md.banks/find"
	_description = "Bank"

class ViewModelListMdBanks(ViewModelListController):
	_name = "list:md.banks"
	_view_name = "md.banks/list"
	_description = "Bank"

class ViewModelFormModalMdBanks(ViewModelFormModalController):
	_name = "form.modal:md.banks"
	_view_name = "md.banks/form.modal"
	_description = "Bank"

class ViewModelFormMdBanks(ViewModelFormController):
	_name = "form:md.banks"
	_view_name = "md.banks/form"
	_description = "Bank"
