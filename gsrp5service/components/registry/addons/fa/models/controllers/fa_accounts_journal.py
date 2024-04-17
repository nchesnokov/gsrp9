from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccountsJournal(ViewModelSearchController):
	_name = "search:fa.accounts.journal"
	_view_name = "fa.accounts.journal/search"
	_description = "General Model Accounts Journal"

class ViewModelFindFaAccountsJournal(ViewModelFindController):
	_name = "find:fa.accounts.journal"
	_view_name = "fa.accounts.journal/find"
	_description = "General Model Accounts Journal"

class ViewModelListFaAccountsJournal(ViewModelListController):
	_name = "list:fa.accounts.journal"
	_view_name = "fa.accounts.journal/list"
	_description = "General Model Accounts Journal"

class ViewModelM2MListFaAccountsType(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.type"
	_view_name = "fa.accounts.type/m2mlist"
	_description = "General Model Accounts Journal"

class ViewModelM2MListFaAccounts(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts"
	_view_name = "fa.accounts/m2mlist"
	_description = "General Model Accounts Journal"

class ViewModelM2MListFaAccountsPaymentMethod(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.payment.method"
	_view_name = "fa.accounts.payment.method/m2mlist"
	_description = "General Model Accounts Journal"

class ViewModelM2MListFaAccountsPaymentMethod(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.payment.method"
	_view_name = "fa.accounts.payment.method/m2mlist"
	_description = "General Model Accounts Journal"

class ViewModelFormModalFaAccountsJournal(ViewModelFormModalController):
	_name = "form.modal:fa.accounts.journal"
	_view_name = "fa.accounts.journal/form.modal"
	_description = "General Model Accounts Journal"

class ViewModelFormFaAccountsJournal(ViewModelFormController):
	_name = "form:fa.accounts.journal"
	_view_name = "fa.accounts.journal/form"
	_description = "General Model Accounts Journal"
