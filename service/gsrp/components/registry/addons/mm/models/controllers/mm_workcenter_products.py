from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmWorkcenterProducts(ViewModelFindController):
	_name = "find:mm.workcenter.products"
	_view_name = "mm.workcenter.products/find"
	_description = "Workcenter Products"

class ViewModelO2MFormMmWorkcenterProducts(ViewModelO2MFormController):
	_name = "o2m-form:mm.workcenter.products"
	_view_name = "mm.workcenter.products/o2m-form"
	_description = "Workcenter Products"

class ViewModelO2MListMmWorkcenterProducts(ViewModelO2MListController):
	_name = "o2m-list:mm.workcenter.products"
	_view_name = "mm.workcenter.products/o2m-list"
	_description = "Workcenter Products"
