from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaFiscalPositionAccountTemplate(ViewModelSearchController):
	_name = "search:fa.fiscal.position.account.template"
	_view_name = "fa.fiscal.position.account.template/search"
	_description = "Template Account Fiscal Mapping"

class ViewModelFindFaFiscalPositionAccountTemplate(ViewModelFindController):
	_name = "find:fa.fiscal.position.account.template"
	_view_name = "fa.fiscal.position.account.template/find"
	_description = "Template Account Fiscal Mapping"

class ViewModelListFaFiscalPositionAccountTemplate(ViewModelListController):
	_name = "list:fa.fiscal.position.account.template"
	_view_name = "fa.fiscal.position.account.template/list"
	_description = "Template Account Fiscal Mapping"

class ViewModelFormModalFaFiscalPositionAccountTemplate(ViewModelFormModalController):
	_name = "form.modal:fa.fiscal.position.account.template"
	_view_name = "fa.fiscal.position.account.template/form.modal"
	_description = "Template Account Fiscal Mapping"

class ViewModelFormFaFiscalPositionAccountTemplate(ViewModelFormController):
	_name = "form:fa.fiscal.position.account.template"
	_view_name = "fa.fiscal.position.account.template/form"
	_description = "Template Account Fiscal Mapping"
