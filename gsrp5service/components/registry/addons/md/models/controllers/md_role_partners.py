from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdRolePartners(ViewModelSearchController):
	_name = "search:md.role.partners"
	_view_name = "md.role.partners/search"
	_description = "Role Partners"

class ViewModelFindMdRolePartners(ViewModelFindController):
	_name = "find:md.role.partners"
	_view_name = "md.role.partners/find"
	_description = "Role Partners"

class ViewModelListMdRolePartners(ViewModelListController):
	_name = "list:md.role.partners"
	_view_name = "md.role.partners/list"
	_description = "Role Partners"

class ViewModelFormModalMdRolePartners(ViewModelFormModalController):
	_name = "form.modal:md.role.partners"
	_view_name = "md.role.partners/form.modal"
	_description = "Role Partners"

class ViewModelFormMdRolePartners(ViewModelFormController):
	_name = "form:md.role.partners"
	_view_name = "md.role.partners/form"
	_description = "Role Partners"
