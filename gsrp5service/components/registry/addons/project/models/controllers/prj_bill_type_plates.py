from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPrjBillTypePlates(ViewModelFindController):
	_name = "find:prj.bill.type.plates"
	_view_name = "prj.bill.type.plates/find"
	_description = "Project Bill Plates"

class ViewModelO2MFormPrjBillTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:prj.bill.type.plates"
	_view_name = "prj.bill.type.plates/o2m-form"
	_description = "Project Bill Plates"

class ViewModelO2MListPrjBillTypePlates(ViewModelO2MListController):
	_name = "o2m-list:prj.bill.type.plates"
	_view_name = "prj.bill.type.plates/o2m-list"
	_description = "Project Bill Plates"
