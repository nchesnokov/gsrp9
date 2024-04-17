from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchWkf1Elements(ViewModelSearchController):
	_name = "search:wkf1.elements"
	_view_name = "wkf1.elements/search"
	_description = "Workflow Element"

class ViewModelFindWkf1Elements(ViewModelFindController):
	_name = "find:wkf1.elements"
	_view_name = "wkf1.elements/find"
	_description = "Workflow Element"

class ViewModelListWkf1Elements(ViewModelListController):
	_name = "list:wkf1.elements"
	_view_name = "wkf1.elements/list"
	_description = "Workflow Element"

class ViewModelFormModalWkf1Elements(ViewModelFormModalController):
	_name = "form.modal:wkf1.elements"
	_view_name = "wkf1.elements/form.modal"
	_description = "Workflow Element"

class ViewModelFormWkf1Elements(ViewModelFormController):
	_name = "form:wkf1.elements"
	_view_name = "wkf1.elements/form"
	_description = "Workflow Element"
