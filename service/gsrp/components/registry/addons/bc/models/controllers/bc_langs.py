from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcLangs(ViewModelSearchController):
	_name = "search:bc.langs"
	_view_name = "bc.langs/search"
	_description = "Langs"

class ViewModelFindBcLangs(ViewModelFindController):
	_name = "find:bc.langs"
	_view_name = "bc.langs/find"
	_description = "Langs"

class ViewModelListBcLangs(ViewModelListController):
	_name = "list:bc.langs"
	_view_name = "bc.langs/list"
	_description = "Langs"

class ViewModelFormModalBcLangs(ViewModelFormModalController):
	_name = "form.modal:bc.langs"
	_view_name = "bc.langs/form.modal"
	_description = "Langs"

class ViewModelFormBcLangs(ViewModelFormController):
	_name = "form:bc.langs"
	_view_name = "bc.langs/form"
	_description = "Langs"
