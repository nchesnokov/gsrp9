from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjStageCategory(ViewModelSearchController):
	_name = "search:prj.stage.category"
	_view_name = "prj.stage.category/search"
	_description = "Category Project Stage"

class ViewModelFindPrjStageCategory(ViewModelFindController):
	_name = "find:prj.stage.category"
	_view_name = "prj.stage.category/find"
	_description = "Category Project Stage"

class ViewModelListPrjStageCategory(ViewModelListController):
	_name = "list:prj.stage.category"
	_view_name = "prj.stage.category/list"
	_description = "Category Project Stage"

class ViewModelFormModalPrjStageCategory(ViewModelFormModalController):
	_name = "form.modal:prj.stage.category"
	_view_name = "prj.stage.category/form.modal"
	_description = "Category Project Stage"

class ViewModelFormPrjStageCategory(ViewModelFormController):
	_name = "form:prj.stage.category"
	_view_name = "prj.stage.category/form"
	_description = "Category Project Stage"

class ViewModelTreePrjStageCategory(ViewModelTreeController):
	_name = "tree:prj.stage.category"
	_view_name = "prj.stage.category/tree"
	_description = "Category Project Stage"
