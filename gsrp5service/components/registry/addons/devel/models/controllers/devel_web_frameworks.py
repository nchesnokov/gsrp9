from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchDevelWebFrameworks(ViewModelSearchController):
	_name = "search:devel.web.frameworks"
	_view_name = "devel.web.frameworks/search"
	_description = "Web Frameworks"

class ViewModelFindDevelWebFrameworks(ViewModelFindController):
	_name = "find:devel.web.frameworks"
	_view_name = "devel.web.frameworks/find"
	_description = "Web Frameworks"

class ViewModelListDevelWebFrameworks(ViewModelListController):
	_name = "list:devel.web.frameworks"
	_view_name = "devel.web.frameworks/list"
	_description = "Web Frameworks"

class ViewModelFormModalDevelWebFrameworks(ViewModelFormModalController):
	_name = "form.modal:devel.web.frameworks"
	_view_name = "devel.web.frameworks/form.modal"
	_description = "Web Frameworks"

class ViewModelFormDevelWebFrameworks(ViewModelFormController):
	_name = "form:devel.web.frameworks"
	_view_name = "devel.web.frameworks/form"
	_description = "Web Frameworks"
