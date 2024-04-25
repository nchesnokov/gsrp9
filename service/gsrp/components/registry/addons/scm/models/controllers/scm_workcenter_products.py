from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmWorkcenterProducts(ViewModelFindController):
	_name = "find:scm.workcenter.products"
	_view_name = "scm.workcenter.products/find"
	_description = "Workcenter Products"

class ViewModelO2MFormScmWorkcenterProducts(ViewModelO2MFormController):
	_name = "o2m-form:scm.workcenter.products"
	_view_name = "scm.workcenter.products/o2m-form"
	_description = "Workcenter Products"

class ViewModelO2MListScmWorkcenterProducts(ViewModelO2MListController):
	_name = "o2m-list:scm.workcenter.products"
	_view_name = "scm.workcenter.products/o2m-list"
	_description = "Workcenter Products"
