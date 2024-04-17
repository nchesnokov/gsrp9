from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjUnitChannelAssigments(ViewModelSearchController):
	_name = "search:prj.unit.channel.assigments"
	_view_name = "prj.unit.channel.assigments/search"
	_description = "Project Unit Of Channel Assigment"

class ViewModelFindPrjUnitChannelAssigments(ViewModelFindController):
	_name = "find:prj.unit.channel.assigments"
	_view_name = "prj.unit.channel.assigments/find"
	_description = "Project Unit Of Channel Assigment"

class ViewModelListPrjUnitChannelAssigments(ViewModelListController):
	_name = "list:prj.unit.channel.assigments"
	_view_name = "prj.unit.channel.assigments/list"
	_description = "Project Unit Of Channel Assigment"

class ViewModelFormModalPrjUnitChannelAssigments(ViewModelFormModalController):
	_name = "form.modal:prj.unit.channel.assigments"
	_view_name = "prj.unit.channel.assigments/form.modal"
	_description = "Project Unit Of Channel Assigment"

class ViewModelFormPrjUnitChannelAssigments(ViewModelFormController):
	_name = "form:prj.unit.channel.assigments"
	_view_name = "prj.unit.channel.assigments/form"
	_description = "Project Unit Of Channel Assigment"
