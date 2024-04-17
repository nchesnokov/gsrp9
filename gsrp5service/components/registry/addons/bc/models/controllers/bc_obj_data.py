from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcObjData(ViewModelSearchController):
	_name = "search:bc.obj.data"
	_view_name = "bc.obj.data/search"
	_description = "Loading Object Relation Data"

class ViewModelFindBcObjData(ViewModelFindController):
	_name = "find:bc.obj.data"
	_view_name = "bc.obj.data/find"
	_description = "Loading Object Relation Data"

class ViewModelListBcObjData(ViewModelListController):
	_name = "list:bc.obj.data"
	_view_name = "bc.obj.data/list"
	_description = "Loading Object Relation Data"

class ViewModelFormModalBcObjData(ViewModelFormModalController):
	_name = "form.modal:bc.obj.data"
	_view_name = "bc.obj.data/form.modal"
	_description = "Loading Object Relation Data"

class ViewModelFormBcObjData(ViewModelFormController):
	_name = "form:bc.obj.data"
	_view_name = "bc.obj.data/form"
	_description = "Loading Object Relation Data"
