from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMmProductionMapCategory(ViewModelSearchController):
	_name = "search:mm.production.map.category"
	_view_name = "mm.production.map.category/search"
	_description = "Category Production Map"

class ViewModelFindMmProductionMapCategory(ViewModelFindController):
	_name = "find:mm.production.map.category"
	_view_name = "mm.production.map.category/find"
	_description = "Category Production Map"

class ViewModelListMmProductionMapCategory(ViewModelListController):
	_name = "list:mm.production.map.category"
	_view_name = "mm.production.map.category/list"
	_description = "Category Production Map"

class ViewModelFormModalMmProductionMapCategory(ViewModelFormModalController):
	_name = "form.modal:mm.production.map.category"
	_view_name = "mm.production.map.category/form.modal"
	_description = "Category Production Map"

class ViewModelFormMmProductionMapCategory(ViewModelFormController):
	_name = "form:mm.production.map.category"
	_view_name = "mm.production.map.category/form"
	_description = "Category Production Map"

class ViewModelTreeMmProductionMapCategory(ViewModelTreeController):
	_name = "tree:mm.production.map.category"
	_view_name = "mm.production.map.category/tree"
	_description = "Category Production Map"
