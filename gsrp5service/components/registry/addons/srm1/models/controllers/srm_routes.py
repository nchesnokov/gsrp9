from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmRoutes(ViewModelSearchController):
	_name = "search:srm.routes"
	_view_name = "srm.routes/search"
	_description = "SRM Route"

class ViewModelFindSrmRoutes(ViewModelFindController):
	_name = "find:srm.routes"
	_view_name = "srm.routes/find"
	_description = "SRM Route"

class ViewModelListSrmRoutes(ViewModelListController):
	_name = "list:srm.routes"
	_view_name = "srm.routes/list"
	_description = "SRM Route"

class ViewModelFormModalSrmRoutes(ViewModelFormModalController):
	_name = "form.modal:srm.routes"
	_view_name = "srm.routes/form.modal"
	_description = "SRM Route"

class ViewModelFormSrmRoutes(ViewModelFormController):
	_name = "form:srm.routes"
	_view_name = "srm.routes/form"
	_description = "SRM Route"
