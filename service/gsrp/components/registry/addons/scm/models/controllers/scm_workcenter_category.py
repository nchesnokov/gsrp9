from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchScmWorkcenterCategory(ViewModelSearchController):
	_name = "search:scm.workcenter.category"
	_view_name = "scm.workcenter.category/search"
	_description = "Category Workcenter"

class ViewModelFindScmWorkcenterCategory(ViewModelFindController):
	_name = "find:scm.workcenter.category"
	_view_name = "scm.workcenter.category/find"
	_description = "Category Workcenter"

class ViewModelListScmWorkcenterCategory(ViewModelListController):
	_name = "list:scm.workcenter.category"
	_view_name = "scm.workcenter.category/list"
	_description = "Category Workcenter"

class ViewModelFormModalScmWorkcenterCategory(ViewModelFormModalController):
	_name = "form.modal:scm.workcenter.category"
	_view_name = "scm.workcenter.category/form.modal"
	_description = "Category Workcenter"

class ViewModelFormScmWorkcenterCategory(ViewModelFormController):
	_name = "form:scm.workcenter.category"
	_view_name = "scm.workcenter.category/form"
	_description = "Category Workcenter"

class ViewModelTreeScmWorkcenterCategory(ViewModelTreeController):
	_name = "tree:scm.workcenter.category"
	_view_name = "scm.workcenter.category/tree"
	_description = "Category Workcenter"
