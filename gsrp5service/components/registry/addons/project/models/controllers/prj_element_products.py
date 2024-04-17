from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPrjElementProducts(ViewModelFindController):
	_name = "find:prj.element.products"
	_view_name = "prj.element.products/find"
	_description = "Project Element Products"

class ViewModelO2MFormPrjElementProducts(ViewModelO2MFormController):
	_name = "o2m-form:prj.element.products"
	_view_name = "prj.element.products/o2m-form"
	_description = "Project Element Products"

class ViewModelO2MListPrjElementProducts(ViewModelO2MListController):
	_name = "o2m-list:prj.element.products"
	_view_name = "prj.element.products/o2m-list"
	_description = "Project Element Products"
