from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaFiscalPositionTaxTemplate(ViewModelSearchController):
	_name = "search:fa.fiscal.position.tax.template"
	_view_name = "fa.fiscal.position.tax.template/search"
	_description = "Template Tax Fiscal Position"

class ViewModelFindFaFiscalPositionTaxTemplate(ViewModelFindController):
	_name = "find:fa.fiscal.position.tax.template"
	_view_name = "fa.fiscal.position.tax.template/find"
	_description = "Template Tax Fiscal Position"

class ViewModelListFaFiscalPositionTaxTemplate(ViewModelListController):
	_name = "list:fa.fiscal.position.tax.template"
	_view_name = "fa.fiscal.position.tax.template/list"
	_description = "Template Tax Fiscal Position"

class ViewModelFormModalFaFiscalPositionTaxTemplate(ViewModelFormModalController):
	_name = "form.modal:fa.fiscal.position.tax.template"
	_view_name = "fa.fiscal.position.tax.template/form.modal"
	_description = "Template Tax Fiscal Position"

class ViewModelFormFaFiscalPositionTaxTemplate(ViewModelFormController):
	_name = "form:fa.fiscal.position.tax.template"
	_view_name = "fa.fiscal.position.tax.template/form"
	_description = "Template Tax Fiscal Position"
