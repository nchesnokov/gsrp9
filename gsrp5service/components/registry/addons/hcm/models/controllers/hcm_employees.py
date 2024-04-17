from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchHcmEmployees(ViewModelSearchController):
	_name = "search:hcm.employees"
	_view_name = "hcm.employees/search"
	_description = "Employees Humam Capital Managament"

class ViewModelFindHcmEmployees(ViewModelFindController):
	_name = "find:hcm.employees"
	_view_name = "hcm.employees/find"
	_description = "Employees Humam Capital Managament"

class ViewModelListHcmEmployees(ViewModelListController):
	_name = "list:hcm.employees"
	_view_name = "hcm.employees/list"
	_description = "Employees Humam Capital Managament"

class ViewModelM2MListHcmEmployeeCategories(ViewModelM2MListController):
	_name = "m2mlist:hcm.employee.categories"
	_view_name = "hcm.employee.categories/m2mlist"
	_description = "Employees Humam Capital Managament"

class ViewModelFormModalHcmEmployees(ViewModelFormModalController):
	_name = "form.modal:hcm.employees"
	_view_name = "hcm.employees/form.modal"
	_description = "Employees Humam Capital Managament"

class ViewModelFormHcmEmployees(ViewModelFormController):
	_name = "form:hcm.employees"
	_view_name = "hcm.employees/form"
	_description = "Employees Humam Capital Managament"

class ViewModelTreeHcmEmployees(ViewModelTreeController):
	_name = "tree:hcm.employees"
	_view_name = "hcm.employees/tree"
	_description = "Employees Humam Capital Managament"
