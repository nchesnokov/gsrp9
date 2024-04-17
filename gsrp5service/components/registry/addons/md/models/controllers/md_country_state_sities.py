from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdCountryStateSities(ViewModelSearchController):
	_name = "search:md.country.state.sities"
	_view_name = "md.country.state.sities/search"
	_description = "Sity Of Country States"

class ViewModelFindMdCountryStateSities(ViewModelFindController):
	_name = "find:md.country.state.sities"
	_view_name = "md.country.state.sities/find"
	_description = "Sity Of Country States"

class ViewModelListMdCountryStateSities(ViewModelListController):
	_name = "list:md.country.state.sities"
	_view_name = "md.country.state.sities/list"
	_description = "Sity Of Country States"

class ViewModelFormModalMdCountryStateSities(ViewModelFormModalController):
	_name = "form.modal:md.country.state.sities"
	_view_name = "md.country.state.sities/form.modal"
	_description = "Sity Of Country States"

class ViewModelFormMdCountryStateSities(ViewModelFormController):
	_name = "form:md.country.state.sities"
	_view_name = "md.country.state.sities/form"
	_description = "Sity Of Country States"
