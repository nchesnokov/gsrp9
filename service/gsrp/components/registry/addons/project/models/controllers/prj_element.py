from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjElement(ViewModelSearchController):
	_name = "search:prj.element"
	_view_name = "prj.element/search"
	_description = "Project Element"

class ViewModelFindPrjElement(ViewModelFindController):
	_name = "find:prj.element"
	_view_name = "prj.element/find"
	_description = "Project Element"

class ViewModelListPrjElement(ViewModelListController):
	_name = "list:prj.element"
	_view_name = "prj.element/list"
	_description = "Project Element"

class ViewModelFormModalPrjElement(ViewModelFormModalController):
	_name = "form.modal:prj.element"
	_view_name = "prj.element/form.modal"
	_description = "Project Element"

class ViewModelFormPrjElement(ViewModelFormController):
	_name = "form:prj.element"
	_view_name = "prj.element/form"
	_description = "Project Element"

class ViewModelTreePrjElement(ViewModelTreeController):
	_name = "tree:prj.element"
	_view_name = "prj.element/tree"
	_description = "Project Element"
