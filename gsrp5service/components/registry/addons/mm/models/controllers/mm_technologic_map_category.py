from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMmTechnologicMapCategory(ViewModelSearchController):
	_name = "search:mm.technologic.map.category"
	_view_name = "mm.technologic.map.category/search"
	_description = "Category Technologic Map"

class ViewModelFindMmTechnologicMapCategory(ViewModelFindController):
	_name = "find:mm.technologic.map.category"
	_view_name = "mm.technologic.map.category/find"
	_description = "Category Technologic Map"

class ViewModelListMmTechnologicMapCategory(ViewModelListController):
	_name = "list:mm.technologic.map.category"
	_view_name = "mm.technologic.map.category/list"
	_description = "Category Technologic Map"

class ViewModelFormModalMmTechnologicMapCategory(ViewModelFormModalController):
	_name = "form.modal:mm.technologic.map.category"
	_view_name = "mm.technologic.map.category/form.modal"
	_description = "Category Technologic Map"

class ViewModelFormMmTechnologicMapCategory(ViewModelFormController):
	_name = "form:mm.technologic.map.category"
	_view_name = "mm.technologic.map.category/form"
	_description = "Category Technologic Map"

class ViewModelTreeMmTechnologicMapCategory(ViewModelTreeController):
	_name = "tree:mm.technologic.map.category"
	_view_name = "mm.technologic.map.category/tree"
	_description = "Category Technologic Map"
