from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdCountryStates(ViewModelSearchController):
	_name = "search:md.country.states"
	_view_name = "md.country.states/search"
	_description = "Country States"

class ViewModelFindMdCountryStates(ViewModelFindController):
	_name = "find:md.country.states"
	_view_name = "md.country.states/find"
	_description = "Country States"

class ViewModelListMdCountryStates(ViewModelListController):
	_name = "list:md.country.states"
	_view_name = "md.country.states/list"
	_description = "Country States"

class ViewModelFormModalMdCountryStates(ViewModelFormModalController):
	_name = "form.modal:md.country.states"
	_view_name = "md.country.states/form.modal"
	_description = "Country States"

class ViewModelFormMdCountryStates(ViewModelFormController):
	_name = "form:md.country.states"
	_view_name = "md.country.states/form"
	_description = "Country States"
