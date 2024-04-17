from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMmMapOpCategory(ViewModelSearchController):
	_name = "search:mm.map.op.category"
	_view_name = "mm.map.op.category/search"
	_description = "Category operation of map"

class ViewModelFindMmMapOpCategory(ViewModelFindController):
	_name = "find:mm.map.op.category"
	_view_name = "mm.map.op.category/find"
	_description = "Category operation of map"

class ViewModelListMmMapOpCategory(ViewModelListController):
	_name = "list:mm.map.op.category"
	_view_name = "mm.map.op.category/list"
	_description = "Category operation of map"

class ViewModelFormModalMmMapOpCategory(ViewModelFormModalController):
	_name = "form.modal:mm.map.op.category"
	_view_name = "mm.map.op.category/form.modal"
	_description = "Category operation of map"

class ViewModelFormMmMapOpCategory(ViewModelFormController):
	_name = "form:mm.map.op.category"
	_view_name = "mm.map.op.category/form"
	_description = "Category operation of map"

class ViewModelTreeMmMapOpCategory(ViewModelTreeController):
	_name = "tree:mm.map.op.category"
	_view_name = "mm.map.op.category/tree"
	_description = "Category operation of map"
