from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaFiscalPositionTemplate(ViewModelSearchController):
	_name = "search:fa.fiscal.position.template"
	_view_name = "fa.fiscal.position.template/search"
	_description = "Template for Fiscal Position"

class ViewModelFindFaFiscalPositionTemplate(ViewModelFindController):
	_name = "find:fa.fiscal.position.template"
	_view_name = "fa.fiscal.position.template/find"
	_description = "Template for Fiscal Position"

class ViewModelListFaFiscalPositionTemplate(ViewModelListController):
	_name = "list:fa.fiscal.position.template"
	_view_name = "fa.fiscal.position.template/list"
	_description = "Template for Fiscal Position"

class ViewModelM2MListMdCountryStates(ViewModelM2MListController):
	_name = "m2mlist:md.country.states"
	_view_name = "md.country.states/m2mlist"
	_description = "Template for Fiscal Position"

class ViewModelFormModalFaFiscalPositionTemplate(ViewModelFormModalController):
	_name = "form.modal:fa.fiscal.position.template"
	_view_name = "fa.fiscal.position.template/form.modal"
	_description = "Template for Fiscal Position"

class ViewModelFormFaFiscalPositionTemplate(ViewModelFormController):
	_name = "form:fa.fiscal.position.template"
	_view_name = "fa.fiscal.position.template/form"
	_description = "Template for Fiscal Position"
