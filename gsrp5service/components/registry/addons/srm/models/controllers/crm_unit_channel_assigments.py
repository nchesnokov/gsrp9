from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmUnitChannelAssigments(ViewModelSearchController):
	_name = "search:crm.unit.channel.assigments"
	_view_name = "crm.unit.channel.assigments/search"
	_description = "CRM Unit Of Channel Assigment"

class ViewModelFindCrmUnitChannelAssigments(ViewModelFindController):
	_name = "find:crm.unit.channel.assigments"
	_view_name = "crm.unit.channel.assigments/find"
	_description = "CRM Unit Of Channel Assigment"

class ViewModelListCrmUnitChannelAssigments(ViewModelListController):
	_name = "list:crm.unit.channel.assigments"
	_view_name = "crm.unit.channel.assigments/list"
	_description = "CRM Unit Of Channel Assigment"

class ViewModelFormModalCrmUnitChannelAssigments(ViewModelFormModalController):
	_name = "form.modal:crm.unit.channel.assigments"
	_view_name = "crm.unit.channel.assigments/form.modal"
	_description = "CRM Unit Of Channel Assigment"

class ViewModelFormCrmUnitChannelAssigments(ViewModelFormController):
	_name = "form:crm.unit.channel.assigments"
	_view_name = "crm.unit.channel.assigments/form"
	_description = "CRM Unit Of Channel Assigment"
