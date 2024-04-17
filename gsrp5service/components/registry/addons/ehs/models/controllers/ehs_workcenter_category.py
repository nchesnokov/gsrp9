from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchEhsWorkcenterCategory(ViewModelSearchController):
	_name = "search:ehs.workcenter.category"
	_view_name = "ehs.workcenter.category/search"
	_description = "Category Workcenter"

class ViewModelFindEhsWorkcenterCategory(ViewModelFindController):
	_name = "find:ehs.workcenter.category"
	_view_name = "ehs.workcenter.category/find"
	_description = "Category Workcenter"

class ViewModelListEhsWorkcenterCategory(ViewModelListController):
	_name = "list:ehs.workcenter.category"
	_view_name = "ehs.workcenter.category/list"
	_description = "Category Workcenter"

class ViewModelFormModalEhsWorkcenterCategory(ViewModelFormModalController):
	_name = "form.modal:ehs.workcenter.category"
	_view_name = "ehs.workcenter.category/form.modal"
	_description = "Category Workcenter"

class ViewModelFormEhsWorkcenterCategory(ViewModelFormController):
	_name = "form:ehs.workcenter.category"
	_view_name = "ehs.workcenter.category/form"
	_description = "Category Workcenter"

class ViewModelTreeEhsWorkcenterCategory(ViewModelTreeController):
	_name = "tree:ehs.workcenter.category"
	_view_name = "ehs.workcenter.category/tree"
	_description = "Category Workcenter"
