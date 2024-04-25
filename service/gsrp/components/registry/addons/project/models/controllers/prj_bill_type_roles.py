from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPrjBillTypeRoles(ViewModelFindController):
	_name = "find:prj.bill.type.roles"
	_view_name = "prj.bill.type.roles/find"
	_description = "Role Project BIll Types"

class ViewModelO2MFormPrjBillTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:prj.bill.type.roles"
	_view_name = "prj.bill.type.roles/o2m-form"
	_description = "Role Project BIll Types"

class ViewModelO2MListPrjBillTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:prj.bill.type.roles"
	_view_name = "prj.bill.type.roles/o2m-list"
	_description = "Role Project BIll Types"
