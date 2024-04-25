from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjResourceCategory(ViewModelSearchController):
	_name = "search:prj.resource.category"
	_view_name = "prj.resource.category/search"
	_description = "Category Project Resource"

class ViewModelFindPrjResourceCategory(ViewModelFindController):
	_name = "find:prj.resource.category"
	_view_name = "prj.resource.category/find"
	_description = "Category Project Resource"

class ViewModelListPrjResourceCategory(ViewModelListController):
	_name = "list:prj.resource.category"
	_view_name = "prj.resource.category/list"
	_description = "Category Project Resource"

class ViewModelFormModalPrjResourceCategory(ViewModelFormModalController):
	_name = "form.modal:prj.resource.category"
	_view_name = "prj.resource.category/form.modal"
	_description = "Category Project Resource"

class ViewModelFormPrjResourceCategory(ViewModelFormController):
	_name = "form:prj.resource.category"
	_view_name = "prj.resource.category/form"
	_description = "Category Project Resource"

class ViewModelTreePrjResourceCategory(ViewModelTreeController):
	_name = "tree:prj.resource.category"
	_view_name = "prj.resource.category/tree"
	_description = "Category Project Resource"
