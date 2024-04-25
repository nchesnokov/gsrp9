from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseUnitChannelAssigments(ViewModelSearchController):
	_name = "search:purchase.unit.channel.assigments"
	_view_name = "purchase.unit.channel.assigments/search"
	_description = "Purchase Unit Of Channel Assigment"

class ViewModelFindPurchaseUnitChannelAssigments(ViewModelFindController):
	_name = "find:purchase.unit.channel.assigments"
	_view_name = "purchase.unit.channel.assigments/find"
	_description = "Purchase Unit Of Channel Assigment"

class ViewModelListPurchaseUnitChannelAssigments(ViewModelListController):
	_name = "list:purchase.unit.channel.assigments"
	_view_name = "purchase.unit.channel.assigments/list"
	_description = "Purchase Unit Of Channel Assigment"

class ViewModelFormModalPurchaseUnitChannelAssigments(ViewModelFormModalController):
	_name = "form.modal:purchase.unit.channel.assigments"
	_view_name = "purchase.unit.channel.assigments/form.modal"
	_description = "Purchase Unit Of Channel Assigment"

class ViewModelFormPurchaseUnitChannelAssigments(ViewModelFormController):
	_name = "form:purchase.unit.channel.assigments"
	_view_name = "purchase.unit.channel.assigments/form"
	_description = "Purchase Unit Of Channel Assigment"
