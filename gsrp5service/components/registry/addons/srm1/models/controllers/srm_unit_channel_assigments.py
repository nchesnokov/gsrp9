from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmUnitChannelAssigments(ViewModelSearchController):
	_name = "search:srm.unit.channel.assigments"
	_view_name = "srm.unit.channel.assigments/search"
	_description = "SRM Unit Of Channel Assigment"

class ViewModelFindSrmUnitChannelAssigments(ViewModelFindController):
	_name = "find:srm.unit.channel.assigments"
	_view_name = "srm.unit.channel.assigments/find"
	_description = "SRM Unit Of Channel Assigment"

class ViewModelListSrmUnitChannelAssigments(ViewModelListController):
	_name = "list:srm.unit.channel.assigments"
	_view_name = "srm.unit.channel.assigments/list"
	_description = "SRM Unit Of Channel Assigment"

class ViewModelFormModalSrmUnitChannelAssigments(ViewModelFormModalController):
	_name = "form.modal:srm.unit.channel.assigments"
	_view_name = "srm.unit.channel.assigments/form.modal"
	_description = "SRM Unit Of Channel Assigment"

class ViewModelFormSrmUnitChannelAssigments(ViewModelFormController):
	_name = "form:srm.unit.channel.assigments"
	_view_name = "srm.unit.channel.assigments/form"
	_description = "SRM Unit Of Channel Assigment"
