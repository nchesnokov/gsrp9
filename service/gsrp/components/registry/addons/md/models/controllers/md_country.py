from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdCountry(ViewModelSearchController):
	_name = "search:md.country"
	_view_name = "md.country/search"
	_description = "Country"

class ViewModelFindMdCountry(ViewModelFindController):
	_name = "find:md.country"
	_view_name = "md.country/find"
	_description = "Country"

class ViewModelListMdCountry(ViewModelListController):
	_name = "list:md.country"
	_view_name = "md.country/list"
	_description = "Country"

class ViewModelM2MListMdCountryGroup(ViewModelM2MListController):
	_name = "m2mlist:md.country.group"
	_view_name = "md.country.group/m2mlist"
	_description = "Country"

class ViewModelFormModalMdCountry(ViewModelFormModalController):
	_name = "form.modal:md.country"
	_view_name = "md.country/form.modal"
	_description = "Country"

class ViewModelFormMdCountry(ViewModelFormController):
	_name = "form:md.country"
	_view_name = "md.country/form"
	_description = "Country"
