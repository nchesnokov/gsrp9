from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCfGroups(ViewModelSearchController):
	_name = "search:cf.groups"
	_view_name = "cf.groups/search"
	_description = "Colobrative Groups"

class ViewModelFindCfGroups(ViewModelFindController):
	_name = "find:cf.groups"
	_view_name = "cf.groups/find"
	_description = "Colobrative Groups"

class ViewModelListCfGroups(ViewModelListController):
	_name = "list:cf.groups"
	_view_name = "cf.groups/list"
	_description = "Colobrative Groups"

class ViewModelM2MListBcUsers(ViewModelM2MListController):
	_name = "m2mlist:bc.users"
	_view_name = "bc.users/m2mlist"
	_description = "Colobrative Groups"

class ViewModelFormModalCfGroups(ViewModelFormModalController):
	_name = "form.modal:cf.groups"
	_view_name = "cf.groups/form.modal"
	_description = "Colobrative Groups"

class ViewModelFormCfGroups(ViewModelFormController):
	_name = "form:cf.groups"
	_view_name = "cf.groups/form"
	_description = "Colobrative Groups"
