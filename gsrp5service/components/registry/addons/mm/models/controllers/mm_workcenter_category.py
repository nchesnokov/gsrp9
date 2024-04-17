from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMmWorkcenterCategory(ViewModelSearchController):
	_name = "search:mm.workcenter.category"
	_view_name = "mm.workcenter.category/search"
	_description = "Category Workcenter"

class ViewModelFindMmWorkcenterCategory(ViewModelFindController):
	_name = "find:mm.workcenter.category"
	_view_name = "mm.workcenter.category/find"
	_description = "Category Workcenter"

class ViewModelListMmWorkcenterCategory(ViewModelListController):
	_name = "list:mm.workcenter.category"
	_view_name = "mm.workcenter.category/list"
	_description = "Category Workcenter"

class ViewModelFormModalMmWorkcenterCategory(ViewModelFormModalController):
	_name = "form.modal:mm.workcenter.category"
	_view_name = "mm.workcenter.category/form.modal"
	_description = "Category Workcenter"

class ViewModelFormMmWorkcenterCategory(ViewModelFormController):
	_name = "form:mm.workcenter.category"
	_view_name = "mm.workcenter.category/form"
	_description = "Category Workcenter"

class ViewModelTreeMmWorkcenterCategory(ViewModelTreeController):
	_name = "tree:mm.workcenter.category"
	_view_name = "mm.workcenter.category/tree"
	_description = "Category Workcenter"
