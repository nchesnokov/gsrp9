from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcClassObjCategories(ViewModelSearchController):
	_name = "search:bc.class.obj.categories"
	_view_name = "bc.class.obj.categories/search"
	_description = "Category Class Objs"

class ViewModelFindBcClassObjCategories(ViewModelFindController):
	_name = "find:bc.class.obj.categories"
	_view_name = "bc.class.obj.categories/find"
	_description = "Category Class Objs"

class ViewModelListBcClassObjCategories(ViewModelListController):
	_name = "list:bc.class.obj.categories"
	_view_name = "bc.class.obj.categories/list"
	_description = "Category Class Objs"

class ViewModelFormModalBcClassObjCategories(ViewModelFormModalController):
	_name = "form.modal:bc.class.obj.categories"
	_view_name = "bc.class.obj.categories/form.modal"
	_description = "Category Class Objs"

class ViewModelFormBcClassObjCategories(ViewModelFormController):
	_name = "form:bc.class.obj.categories"
	_view_name = "bc.class.obj.categories/form"
	_description = "Category Class Objs"
