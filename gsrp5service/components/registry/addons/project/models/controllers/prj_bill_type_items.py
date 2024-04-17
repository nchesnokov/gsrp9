from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPrjBillTypeItems(ViewModelFindController):
	_name = "find:prj.bill.type.items"
	_view_name = "prj.bill.type.items/find"
	_description = "Plates Of Project Bill Items"

class ViewModelO2MFormPrjBillTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:prj.bill.type.items"
	_view_name = "prj.bill.type.items/o2m-form"
	_description = "Plates Of Project Bill Items"

class ViewModelO2MListPrjBillTypeItems(ViewModelO2MListController):
	_name = "o2m-list:prj.bill.type.items"
	_view_name = "prj.bill.type.items/o2m-list"
	_description = "Plates Of Project Bill Items"
