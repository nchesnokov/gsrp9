from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaTaxTemplate(ViewModelSearchController):
	_name = "search:fa.tax.template"
	_view_name = "fa.tax.template/search"
	_description = "General Model Templates for Taxes"

class ViewModelFindFaTaxTemplate(ViewModelFindController):
	_name = "find:fa.tax.template"
	_view_name = "fa.tax.template/find"
	_description = "General Model Templates for Taxes"

class ViewModelListFaTaxTemplate(ViewModelListController):
	_name = "list:fa.tax.template"
	_view_name = "fa.tax.template/list"
	_description = "General Model Templates for Taxes"

class ViewModelM2MListFaTaxTemplate(ViewModelM2MListController):
	_name = "m2mlist:fa.tax.template"
	_view_name = "fa.tax.template/m2mlist"
	_description = "General Model Templates for Taxes"

class ViewModelM2MListFaAccountsTag(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.tag"
	_view_name = "fa.accounts.tag/m2mlist"
	_description = "General Model Templates for Taxes"

class ViewModelFormModalFaTaxTemplate(ViewModelFormModalController):
	_name = "form.modal:fa.tax.template"
	_view_name = "fa.tax.template/form.modal"
	_description = "General Model Templates for Taxes"

class ViewModelFormFaTaxTemplate(ViewModelFormController):
	_name = "form:fa.tax.template"
	_view_name = "fa.tax.template/form"
	_description = "General Model Templates for Taxes"
