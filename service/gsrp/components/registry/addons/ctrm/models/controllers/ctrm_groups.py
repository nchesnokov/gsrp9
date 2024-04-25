from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmGroups(ViewModelSearchController):
	_name = "search:ctrm.groups"
	_view_name = "ctrm.groups/search"
	_description = "CTRM Groups"

class ViewModelFindCtrmGroups(ViewModelFindController):
	_name = "find:ctrm.groups"
	_view_name = "ctrm.groups/find"
	_description = "CTRM Groups"

class ViewModelListCtrmGroups(ViewModelListController):
	_name = "list:ctrm.groups"
	_view_name = "ctrm.groups/list"
	_description = "CTRM Groups"

class ViewModelFormModalCtrmGroups(ViewModelFormModalController):
	_name = "form.modal:ctrm.groups"
	_view_name = "ctrm.groups/form.modal"
	_description = "CTRM Groups"

class ViewModelFormCtrmGroups(ViewModelFormController):
	_name = "form:ctrm.groups"
	_view_name = "ctrm.groups/form"
	_description = "CTRM Groups"
