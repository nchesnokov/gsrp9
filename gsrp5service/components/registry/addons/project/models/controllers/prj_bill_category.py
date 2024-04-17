from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjBillCategory(ViewModelSearchController):
	_name = "search:prj.bill.category"
	_view_name = "prj.bill.category/search"
	_description = "Category Project Bill"

class ViewModelFindPrjBillCategory(ViewModelFindController):
	_name = "find:prj.bill.category"
	_view_name = "prj.bill.category/find"
	_description = "Category Project Bill"

class ViewModelListPrjBillCategory(ViewModelListController):
	_name = "list:prj.bill.category"
	_view_name = "prj.bill.category/list"
	_description = "Category Project Bill"

class ViewModelFormModalPrjBillCategory(ViewModelFormModalController):
	_name = "form.modal:prj.bill.category"
	_view_name = "prj.bill.category/form.modal"
	_description = "Category Project Bill"

class ViewModelFormPrjBillCategory(ViewModelFormController):
	_name = "form:prj.bill.category"
	_view_name = "prj.bill.category/form"
	_description = "Category Project Bill"

class ViewModelTreePrjBillCategory(ViewModelTreeController):
	_name = "tree:prj.bill.category"
	_view_name = "prj.bill.category/tree"
	_description = "Category Project Bill"
