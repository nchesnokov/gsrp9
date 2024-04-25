from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmSegments(ViewModelSearchController):
	_name = "search:crm.segments"
	_view_name = "crm.segments/search"
	_description = "CRM Segments"

class ViewModelFindCrmSegments(ViewModelFindController):
	_name = "find:crm.segments"
	_view_name = "crm.segments/find"
	_description = "CRM Segments"

class ViewModelListCrmSegments(ViewModelListController):
	_name = "list:crm.segments"
	_view_name = "crm.segments/list"
	_description = "CRM Segments"

class ViewModelFormModalCrmSegments(ViewModelFormModalController):
	_name = "form.modal:crm.segments"
	_view_name = "crm.segments/form.modal"
	_description = "CRM Segments"

class ViewModelFormCrmSegments(ViewModelFormController):
	_name = "form:crm.segments"
	_view_name = "crm.segments/form"
	_description = "CRM Segments"
