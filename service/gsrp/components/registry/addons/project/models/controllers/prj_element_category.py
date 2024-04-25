from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjElementCategory(ViewModelSearchController):
	_name = "search:prj.element.category"
	_view_name = "prj.element.category/search"
	_description = "Category Project Element"

class ViewModelFindPrjElementCategory(ViewModelFindController):
	_name = "find:prj.element.category"
	_view_name = "prj.element.category/find"
	_description = "Category Project Element"

class ViewModelListPrjElementCategory(ViewModelListController):
	_name = "list:prj.element.category"
	_view_name = "prj.element.category/list"
	_description = "Category Project Element"

class ViewModelFormModalPrjElementCategory(ViewModelFormModalController):
	_name = "form.modal:prj.element.category"
	_view_name = "prj.element.category/form.modal"
	_description = "Category Project Element"

class ViewModelFormPrjElementCategory(ViewModelFormController):
	_name = "form:prj.element.category"
	_view_name = "prj.element.category/form"
	_description = "Category Project Element"

class ViewModelTreePrjElementCategory(ViewModelTreeController):
	_name = "tree:prj.element.category"
	_view_name = "prj.element.category/tree"
	_description = "Category Project Element"
