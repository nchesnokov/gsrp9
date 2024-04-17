from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchWkfElements(ViewModelSearchController):
	_name = "search:wkf.elements"
	_view_name = "wkf.elements/search"
	_description = "Workflow Element"

class ViewModelFindWkfElements(ViewModelFindController):
	_name = "find:wkf.elements"
	_view_name = "wkf.elements/find"
	_description = "Workflow Element"

class ViewModelListWkfElements(ViewModelListController):
	_name = "list:wkf.elements"
	_view_name = "wkf.elements/list"
	_description = "Workflow Element"

class ViewModelFormModalWkfElements(ViewModelFormModalController):
	_name = "form.modal:wkf.elements"
	_view_name = "wkf.elements/form.modal"
	_description = "Workflow Element"

class ViewModelFormWkfElements(ViewModelFormController):
	_name = "form:wkf.elements"
	_view_name = "wkf.elements/form"
	_description = "Workflow Element"

class ViewModelTreeWkfElements(ViewModelTreeController):
	_name = "tree:wkf.elements"
	_view_name = "wkf.elements/tree"
	_description = "Workflow Element"
