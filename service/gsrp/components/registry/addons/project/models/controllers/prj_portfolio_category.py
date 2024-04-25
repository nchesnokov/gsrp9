from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjPortfolioCategory(ViewModelSearchController):
	_name = "search:prj.portfolio.category"
	_view_name = "prj.portfolio.category/search"
	_description = "Category Project Portfolio"

class ViewModelFindPrjPortfolioCategory(ViewModelFindController):
	_name = "find:prj.portfolio.category"
	_view_name = "prj.portfolio.category/find"
	_description = "Category Project Portfolio"

class ViewModelListPrjPortfolioCategory(ViewModelListController):
	_name = "list:prj.portfolio.category"
	_view_name = "prj.portfolio.category/list"
	_description = "Category Project Portfolio"

class ViewModelFormModalPrjPortfolioCategory(ViewModelFormModalController):
	_name = "form.modal:prj.portfolio.category"
	_view_name = "prj.portfolio.category/form.modal"
	_description = "Category Project Portfolio"

class ViewModelFormPrjPortfolioCategory(ViewModelFormController):
	_name = "form:prj.portfolio.category"
	_view_name = "prj.portfolio.category/form"
	_description = "Category Project Portfolio"

class ViewModelTreePrjPortfolioCategory(ViewModelTreeController):
	_name = "tree:prj.portfolio.category"
	_view_name = "prj.portfolio.category/tree"
	_description = "Category Project Portfolio"
