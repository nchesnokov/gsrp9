from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdVatCode(ViewModelSearchController):
	_name = "search:md.vat.code"
	_view_name = "md.vat.code/search"
	_description = "Vat Code"

class ViewModelFindMdVatCode(ViewModelFindController):
	_name = "find:md.vat.code"
	_view_name = "md.vat.code/find"
	_description = "Vat Code"

class ViewModelListMdVatCode(ViewModelListController):
	_name = "list:md.vat.code"
	_view_name = "md.vat.code/list"
	_description = "Vat Code"

class ViewModelFormModalMdVatCode(ViewModelFormModalController):
	_name = "form.modal:md.vat.code"
	_view_name = "md.vat.code/form.modal"
	_description = "Vat Code"

class ViewModelFormMdVatCode(ViewModelFormController):
	_name = "form:md.vat.code"
	_view_name = "md.vat.code/form"
	_description = "Vat Code"
