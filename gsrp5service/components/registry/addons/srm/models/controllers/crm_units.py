from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmUnits(ViewModelSearchController):
	_name = "search:crm.units"
	_view_name = "crm.units/search"
	_description = "CRM Units"

class ViewModelFindCrmUnits(ViewModelFindController):
	_name = "find:crm.units"
	_view_name = "crm.units/find"
	_description = "CRM Units"

class ViewModelListCrmUnits(ViewModelListController):
	_name = "list:crm.units"
	_view_name = "crm.units/list"
	_description = "CRM Units"

class ViewModelM2MListMdCompany(ViewModelM2MListController):
	_name = "m2mlist:md.company"
	_view_name = "md.company/m2mlist"
	_description = "CRM Units"

class ViewModelFormModalCrmUnits(ViewModelFormModalController):
	_name = "form.modal:crm.units"
	_view_name = "crm.units/form.modal"
	_description = "CRM Units"

class ViewModelFormCrmUnits(ViewModelFormController):
	_name = "form:crm.units"
	_view_name = "crm.units/form"
	_description = "CRM Units"
