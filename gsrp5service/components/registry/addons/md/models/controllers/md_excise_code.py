from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdExciseCode(ViewModelSearchController):
	_name = "search:md.excise.code"
	_view_name = "md.excise.code/search"
	_description = "Excise Code"

class ViewModelFindMdExciseCode(ViewModelFindController):
	_name = "find:md.excise.code"
	_view_name = "md.excise.code/find"
	_description = "Excise Code"

class ViewModelListMdExciseCode(ViewModelListController):
	_name = "list:md.excise.code"
	_view_name = "md.excise.code/list"
	_description = "Excise Code"

class ViewModelFormModalMdExciseCode(ViewModelFormModalController):
	_name = "form.modal:md.excise.code"
	_view_name = "md.excise.code/form.modal"
	_description = "Excise Code"

class ViewModelFormMdExciseCode(ViewModelFormController):
	_name = "form:md.excise.code"
	_view_name = "md.excise.code/form"
	_description = "Excise Code"
