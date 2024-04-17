from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjBillTypes(ViewModelSearchController):
	_name = "search:prj.bill.types"
	_view_name = "prj.bill.types/search"
	_description = "Types Project Bill"

class ViewModelFindPrjBillTypes(ViewModelFindController):
	_name = "find:prj.bill.types"
	_view_name = "prj.bill.types/find"
	_description = "Types Project Bill"

class ViewModelListPrjBillTypes(ViewModelListController):
	_name = "list:prj.bill.types"
	_view_name = "prj.bill.types/list"
	_description = "Types Project Bill"

class ViewModelFormModalPrjBillTypes(ViewModelFormModalController):
	_name = "form.modal:prj.bill.types"
	_view_name = "prj.bill.types/form.modal"
	_description = "Types Project Bill"

class ViewModelFormPrjBillTypes(ViewModelFormController):
	_name = "form:prj.bill.types"
	_view_name = "prj.bill.types/form"
	_description = "Types Project Bill"
