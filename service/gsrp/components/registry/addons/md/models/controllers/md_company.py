from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdCompany(ViewModelSearchController):
	_name = "search:md.company"
	_view_name = "md.company/search"
	_description = "Company"

class ViewModelFindMdCompany(ViewModelFindController):
	_name = "find:md.company"
	_view_name = "md.company/find"
	_description = "Company"

class ViewModelListMdCompany(ViewModelListController):
	_name = "list:md.company"
	_view_name = "md.company/list"
	_description = "Company"

class ViewModelFormModalMdCompany(ViewModelFormModalController):
	_name = "form.modal:md.company"
	_view_name = "md.company/form.modal"
	_description = "Company"

class ViewModelFormMdCompany(ViewModelFormController):
	_name = "form:md.company"
	_view_name = "md.company/form"
	_description = "Company"
