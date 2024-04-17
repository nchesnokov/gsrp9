from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmSubdivisions(ViewModelSearchController):
	_name = "search:crm.subdivisions"
	_view_name = "crm.subdivisions/search"
	_description = "CRM Subdivisions"

class ViewModelFindCrmSubdivisions(ViewModelFindController):
	_name = "find:crm.subdivisions"
	_view_name = "crm.subdivisions/find"
	_description = "CRM Subdivisions"

class ViewModelListCrmSubdivisions(ViewModelListController):
	_name = "list:crm.subdivisions"
	_view_name = "crm.subdivisions/list"
	_description = "CRM Subdivisions"

class ViewModelFormModalCrmSubdivisions(ViewModelFormModalController):
	_name = "form.modal:crm.subdivisions"
	_view_name = "crm.subdivisions/form.modal"
	_description = "CRM Subdivisions"

class ViewModelFormCrmSubdivisions(ViewModelFormController):
	_name = "form:crm.subdivisions"
	_view_name = "crm.subdivisions/form"
	_description = "CRM Subdivisions"
