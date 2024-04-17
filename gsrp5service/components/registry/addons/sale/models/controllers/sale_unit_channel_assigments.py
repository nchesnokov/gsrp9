from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleUnitChannelAssigments(ViewModelSearchController):
	_name = "search:sale.unit.channel.assigments"
	_view_name = "sale.unit.channel.assigments/search"
	_description = "Sale Unit Of Channel Assigment"

class ViewModelFindSaleUnitChannelAssigments(ViewModelFindController):
	_name = "find:sale.unit.channel.assigments"
	_view_name = "sale.unit.channel.assigments/find"
	_description = "Sale Unit Of Channel Assigment"

class ViewModelListSaleUnitChannelAssigments(ViewModelListController):
	_name = "list:sale.unit.channel.assigments"
	_view_name = "sale.unit.channel.assigments/list"
	_description = "Sale Unit Of Channel Assigment"

class ViewModelFormModalSaleUnitChannelAssigments(ViewModelFormModalController):
	_name = "form.modal:sale.unit.channel.assigments"
	_view_name = "sale.unit.channel.assigments/form.modal"
	_description = "Sale Unit Of Channel Assigment"

class ViewModelFormSaleUnitChannelAssigments(ViewModelFormController):
	_name = "form:sale.unit.channel.assigments"
	_view_name = "sale.unit.channel.assigments/form"
	_description = "Sale Unit Of Channel Assigment"
