from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleUnits(ViewModelSearchController):
	_name = "search:sale.units"
	_view_name = "sale.units/search"
	_description = "Sale Units"

class ViewModelFindSaleUnits(ViewModelFindController):
	_name = "find:sale.units"
	_view_name = "sale.units/find"
	_description = "Sale Units"

class ViewModelListSaleUnits(ViewModelListController):
	_name = "list:sale.units"
	_view_name = "sale.units/list"
	_description = "Sale Units"

class ViewModelM2MListMdCompany(ViewModelM2MListController):
	_name = "m2mlist:md.company"
	_view_name = "md.company/m2mlist"
	_description = "Sale Units"

class ViewModelFormModalSaleUnits(ViewModelFormModalController):
	_name = "form.modal:sale.units"
	_view_name = "sale.units/form.modal"
	_description = "Sale Units"

class ViewModelFormSaleUnits(ViewModelFormController):
	_name = "form:sale.units"
	_view_name = "sale.units/form"
	_description = "Sale Units"
