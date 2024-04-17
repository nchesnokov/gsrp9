from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCmCorporations(ViewModelSearchController):
	_name = "search:cm.corporations"
	_view_name = "cm.corporations/search"
	_description = "Corporations"

class ViewModelFindCmCorporations(ViewModelFindController):
	_name = "find:cm.corporations"
	_view_name = "cm.corporations/find"
	_description = "Corporations"

class ViewModelListCmCorporations(ViewModelListController):
	_name = "list:cm.corporations"
	_view_name = "cm.corporations/list"
	_description = "Corporations"

class ViewModelFormModalCmCorporations(ViewModelFormModalController):
	_name = "form.modal:cm.corporations"
	_view_name = "cm.corporations/form.modal"
	_description = "Corporations"

class ViewModelFormCmCorporations(ViewModelFormController):
	_name = "form:cm.corporations"
	_view_name = "cm.corporations/form"
	_description = "Corporations"
