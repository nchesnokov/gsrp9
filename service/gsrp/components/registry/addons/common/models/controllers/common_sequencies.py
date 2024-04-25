from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCommonSequencies(ViewModelSearchController):
	_name = "search:common.sequencies"
	_view_name = "common.sequencies/search"
	_description = "Common Sequencies"

class ViewModelFindCommonSequencies(ViewModelFindController):
	_name = "find:common.sequencies"
	_view_name = "common.sequencies/find"
	_description = "Common Sequencies"

class ViewModelListCommonSequencies(ViewModelListController):
	_name = "list:common.sequencies"
	_view_name = "common.sequencies/list"
	_description = "Common Sequencies"

class ViewModelFormModalCommonSequencies(ViewModelFormModalController):
	_name = "form.modal:common.sequencies"
	_view_name = "common.sequencies/form.modal"
	_description = "Common Sequencies"

class ViewModelFormCommonSequencies(ViewModelFormController):
	_name = "form:common.sequencies"
	_view_name = "common.sequencies/form"
	_description = "Common Sequencies"
