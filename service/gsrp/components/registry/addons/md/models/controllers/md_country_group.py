from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdCountryGroup(ViewModelSearchController):
	_name = "search:md.country.group"
	_view_name = "md.country.group/search"
	_description = "Country Group"

class ViewModelFindMdCountryGroup(ViewModelFindController):
	_name = "find:md.country.group"
	_view_name = "md.country.group/find"
	_description = "Country Group"

class ViewModelListMdCountryGroup(ViewModelListController):
	_name = "list:md.country.group"
	_view_name = "md.country.group/list"
	_description = "Country Group"

class ViewModelM2MListMdCountry(ViewModelM2MListController):
	_name = "m2mlist:md.country"
	_view_name = "md.country/m2mlist"
	_description = "Country Group"

class ViewModelFormModalMdCountryGroup(ViewModelFormModalController):
	_name = "form.modal:md.country.group"
	_view_name = "md.country.group/form.modal"
	_description = "Country Group"

class ViewModelFormMdCountryGroup(ViewModelFormController):
	_name = "form:md.country.group"
	_view_name = "md.country.group/form"
	_description = "Country Group"
