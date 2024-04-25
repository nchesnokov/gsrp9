from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcWebFrameworks(ViewModelSearchController):
	_name = "search:bc.web.frameworks"
	_view_name = "bc.web.frameworks/search"
	_description = "Web Frameworks"

class ViewModelFindBcWebFrameworks(ViewModelFindController):
	_name = "find:bc.web.frameworks"
	_view_name = "bc.web.frameworks/find"
	_description = "Web Frameworks"

class ViewModelListBcWebFrameworks(ViewModelListController):
	_name = "list:bc.web.frameworks"
	_view_name = "bc.web.frameworks/list"
	_description = "Web Frameworks"

class ViewModelFormModalBcWebFrameworks(ViewModelFormModalController):
	_name = "form.modal:bc.web.frameworks"
	_view_name = "bc.web.frameworks/form.modal"
	_description = "Web Frameworks"

class ViewModelFormBcWebFrameworks(ViewModelFormController):
	_name = "form:bc.web.frameworks"
	_view_name = "bc.web.frameworks/form"
	_description = "Web Frameworks"
