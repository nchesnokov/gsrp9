from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchDevelMessages(ViewModelSearchController):
	_name = "search:devel.messages"
	_view_name = "devel.messages/search"
	_description = "Messages"

class ViewModelFindDevelMessages(ViewModelFindController):
	_name = "find:devel.messages"
	_view_name = "devel.messages/find"
	_description = "Messages"

class ViewModelListDevelMessages(ViewModelListController):
	_name = "list:devel.messages"
	_view_name = "devel.messages/list"
	_description = "Messages"

class ViewModelFormModalDevelMessages(ViewModelFormModalController):
	_name = "form.modal:devel.messages"
	_view_name = "devel.messages/form.modal"
	_description = "Messages"

class ViewModelFormDevelMessages(ViewModelFormController):
	_name = "form:devel.messages"
	_view_name = "devel.messages/form"
	_description = "Messages"
