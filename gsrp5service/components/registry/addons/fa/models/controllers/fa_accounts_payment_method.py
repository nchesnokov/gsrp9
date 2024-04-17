from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccountsPaymentMethod(ViewModelSearchController):
	_name = "search:fa.accounts.payment.method"
	_view_name = "fa.accounts.payment.method/search"
	_description = "Genaral  ModelPayment Methods"

class ViewModelFindFaAccountsPaymentMethod(ViewModelFindController):
	_name = "find:fa.accounts.payment.method"
	_view_name = "fa.accounts.payment.method/find"
	_description = "Genaral  ModelPayment Methods"

class ViewModelListFaAccountsPaymentMethod(ViewModelListController):
	_name = "list:fa.accounts.payment.method"
	_view_name = "fa.accounts.payment.method/list"
	_description = "Genaral  ModelPayment Methods"

class ViewModelFormModalFaAccountsPaymentMethod(ViewModelFormModalController):
	_name = "form.modal:fa.accounts.payment.method"
	_view_name = "fa.accounts.payment.method/form.modal"
	_description = "Genaral  ModelPayment Methods"

class ViewModelFormFaAccountsPaymentMethod(ViewModelFormController):
	_name = "form:fa.accounts.payment.method"
	_view_name = "fa.accounts.payment.method/form"
	_description = "Genaral  ModelPayment Methods"
