from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchHcmEmployeeCategories(ViewModelSearchController):
	_name = "search:hcm.employee.categories"
	_view_name = "hcm.employee.categories/search"
	_description = "Employee Category"

class ViewModelFindHcmEmployeeCategories(ViewModelFindController):
	_name = "find:hcm.employee.categories"
	_view_name = "hcm.employee.categories/find"
	_description = "Employee Category"

class ViewModelListHcmEmployeeCategories(ViewModelListController):
	_name = "list:hcm.employee.categories"
	_view_name = "hcm.employee.categories/list"
	_description = "Employee Category"

class ViewModelM2MListHcmEmployees(ViewModelM2MListController):
	_name = "m2mlist:hcm.employees"
	_view_name = "hcm.employees/m2mlist"
	_description = "Employee Category"

class ViewModelFormModalHcmEmployeeCategories(ViewModelFormModalController):
	_name = "form.modal:hcm.employee.categories"
	_view_name = "hcm.employee.categories/form.modal"
	_description = "Employee Category"

class ViewModelFormHcmEmployeeCategories(ViewModelFormController):
	_name = "form:hcm.employee.categories"
	_view_name = "hcm.employee.categories/form"
	_description = "Employee Category"
