from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchDevelAreaMessages(ViewModelSearchController):
	_name = "search:devel.area.messages"
	_view_name = "devel.area.messages/search"
	_description = "Area Messages"

class ViewModelFindDevelAreaMessages(ViewModelFindController):
	_name = "find:devel.area.messages"
	_view_name = "devel.area.messages/find"
	_description = "Area Messages"

class ViewModelListDevelAreaMessages(ViewModelListController):
	_name = "list:devel.area.messages"
	_view_name = "devel.area.messages/list"
	_description = "Area Messages"

class ViewModelFormModalDevelAreaMessages(ViewModelFormModalController):
	_name = "form.modal:devel.area.messages"
	_view_name = "devel.area.messages/form.modal"
	_description = "Area Messages"

class ViewModelFormDevelAreaMessages(ViewModelFormController):
	_name = "form:devel.area.messages"
	_view_name = "devel.area.messages/form"
	_description = "Area Messages"
