from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchStLocation(ViewModelSearchController):
	_name = "search:st.location"
	_view_name = "st.location/search"
	_description = "Stock Location"

class ViewModelFindStLocation(ViewModelFindController):
	_name = "find:st.location"
	_view_name = "st.location/find"
	_description = "Stock Location"

class ViewModelListStLocation(ViewModelListController):
	_name = "list:st.location"
	_view_name = "st.location/list"
	_description = "Stock Location"

class ViewModelFormModalStLocation(ViewModelFormModalController):
	_name = "form.modal:st.location"
	_view_name = "st.location/form.modal"
	_description = "Stock Location"

class ViewModelFormStLocation(ViewModelFormController):
	_name = "form:st.location"
	_view_name = "st.location/form"
	_description = "Stock Location"

class ViewModelTreeStLocation(ViewModelTreeController):
	_name = "tree:st.location"
	_view_name = "st.location/tree"
	_description = "Stock Location"
