from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsWorkcenterProducts(ViewModelFindController):
	_name = "find:ehs.workcenter.products"
	_view_name = "ehs.workcenter.products/find"
	_description = "Workcenter Products"

class ViewModelO2MFormEhsWorkcenterProducts(ViewModelO2MFormController):
	_name = "o2m-form:ehs.workcenter.products"
	_view_name = "ehs.workcenter.products/o2m-form"
	_description = "Workcenter Products"

class ViewModelO2MListEhsWorkcenterProducts(ViewModelO2MListController):
	_name = "o2m-list:ehs.workcenter.products"
	_view_name = "ehs.workcenter.products/o2m-list"
	_description = "Workcenter Products"
