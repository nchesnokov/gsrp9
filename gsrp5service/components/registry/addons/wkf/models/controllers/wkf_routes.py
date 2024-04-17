from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchWkfRoutes(ViewModelSearchController):
	_name = "search:wkf.routes"
	_view_name = "wkf.routes/search"
	_description = "Workflow Routes"

class ViewModelFindWkfRoutes(ViewModelFindController):
	_name = "find:wkf.routes"
	_view_name = "wkf.routes/find"
	_description = "Workflow Routes"

class ViewModelListWkfRoutes(ViewModelListController):
	_name = "list:wkf.routes"
	_view_name = "wkf.routes/list"
	_description = "Workflow Routes"

class ViewModelFormModalWkfRoutes(ViewModelFormModalController):
	_name = "form.modal:wkf.routes"
	_view_name = "wkf.routes/form.modal"
	_description = "Workflow Routes"

class ViewModelFormWkfRoutes(ViewModelFormController):
	_name = "form:wkf.routes"
	_view_name = "wkf.routes/form"
	_description = "Workflow Routes"
