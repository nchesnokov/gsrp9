from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchStStock(ViewModelSearchController):
	_name = "search:st.stock"
	_view_name = "st.stock/search"
	_description = "General Stock"

class ViewModelFindStStock(ViewModelFindController):
	_name = "find:st.stock"
	_view_name = "st.stock/find"
	_description = "General Stock"

class ViewModelListStStock(ViewModelListController):
	_name = "list:st.stock"
	_view_name = "st.stock/list"
	_description = "General Stock"

class ViewModelFormModalStStock(ViewModelFormModalController):
	_name = "form.modal:st.stock"
	_view_name = "st.stock/form.modal"
	_description = "General Stock"

class ViewModelFormStStock(ViewModelFormController):
	_name = "form:st.stock"
	_view_name = "st.stock/form"
	_description = "General Stock"
