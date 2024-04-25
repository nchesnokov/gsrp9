from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcUsers(ViewModelSearchController):
	_name = "search:bc.users"
	_view_name = "bc.users/search"
	_description = "Users"

class ViewModelFindBcUsers(ViewModelFindController):
	_name = "find:bc.users"
	_view_name = "bc.users/find"
	_description = "Users"

class ViewModelListBcUsers(ViewModelListController):
	_name = "list:bc.users"
	_view_name = "bc.users/list"
	_description = "Users"

class ViewModelFormModalBcUsers(ViewModelFormModalController):
	_name = "form.modal:bc.users"
	_view_name = "bc.users/form.modal"
	_description = "Users"

class ViewModelFormBcUsers(ViewModelFormController):
	_name = "form:bc.users"
	_view_name = "bc.users/form"
	_description = "Users"
