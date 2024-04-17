from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMlCategory(ViewModelSearchController):
	_name = "search:ml.category"
	_view_name = "ml.category/search"
	_description = "Mashine Learning Category"

class ViewModelFindMlCategory(ViewModelFindController):
	_name = "find:ml.category"
	_view_name = "ml.category/find"
	_description = "Mashine Learning Category"

class ViewModelListMlCategory(ViewModelListController):
	_name = "list:ml.category"
	_view_name = "ml.category/list"
	_description = "Mashine Learning Category"

class ViewModelFormModalMlCategory(ViewModelFormModalController):
	_name = "form.modal:ml.category"
	_view_name = "ml.category/form.modal"
	_description = "Mashine Learning Category"

class ViewModelFormMlCategory(ViewModelFormController):
	_name = "form:ml.category"
	_view_name = "ml.category/form"
	_description = "Mashine Learning Category"
