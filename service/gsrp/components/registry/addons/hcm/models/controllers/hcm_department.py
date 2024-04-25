from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchHcmDepartment(ViewModelSearchController):
	_name = "search:hcm.department"
	_view_name = "hcm.department/search"
	_description = "HR Department"

class ViewModelFindHcmDepartment(ViewModelFindController):
	_name = "find:hcm.department"
	_view_name = "hcm.department/find"
	_description = "HR Department"

class ViewModelListHcmDepartment(ViewModelListController):
	_name = "list:hcm.department"
	_view_name = "hcm.department/list"
	_description = "HR Department"

class ViewModelFormModalHcmDepartment(ViewModelFormModalController):
	_name = "form.modal:hcm.department"
	_view_name = "hcm.department/form.modal"
	_description = "HR Department"

class ViewModelFormHcmDepartment(ViewModelFormController):
	_name = "form:hcm.department"
	_view_name = "hcm.department/form"
	_description = "HR Department"

class ViewModelTreeHcmDepartment(ViewModelTreeController):
	_name = "tree:hcm.department"
	_view_name = "hcm.department/tree"
	_description = "HR Department"
