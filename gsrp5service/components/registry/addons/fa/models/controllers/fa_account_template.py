from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccountTemplate(ViewModelSearchController):
	_name = "search:fa.account.template"
	_view_name = "fa.account.template/search"
	_description = "Templates for Accounts"

class ViewModelFindFaAccountTemplate(ViewModelFindController):
	_name = "find:fa.account.template"
	_view_name = "fa.account.template/find"
	_description = "Templates for Accounts"

class ViewModelListFaAccountTemplate(ViewModelListController):
	_name = "list:fa.account.template"
	_view_name = "fa.account.template/list"
	_description = "Templates for Accounts"

class ViewModelM2MListFaTaxTemplate(ViewModelM2MListController):
	_name = "m2mlist:fa.tax.template"
	_view_name = "fa.tax.template/m2mlist"
	_description = "Templates for Accounts"

class ViewModelM2MListFaAccountsTag(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.tag"
	_view_name = "fa.accounts.tag/m2mlist"
	_description = "Templates for Accounts"

class ViewModelFormModalFaAccountTemplate(ViewModelFormModalController):
	_name = "form.modal:fa.account.template"
	_view_name = "fa.account.template/form.modal"
	_description = "Templates for Accounts"

class ViewModelFormFaAccountTemplate(ViewModelFormController):
	_name = "form:fa.account.template"
	_view_name = "fa.account.template/form"
	_description = "Templates for Accounts"
