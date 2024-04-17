from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchBcClassModelCategories(ViewModelSearchController):
	_name = "search:bc.class.model.categories"
	_view_name = "bc.class.model.categories/search"
	_description = "Category Class Models"

class ViewModelFindBcClassModelCategories(ViewModelFindController):
	_name = "find:bc.class.model.categories"
	_view_name = "bc.class.model.categories/find"
	_description = "Category Class Models"

class ViewModelListBcClassModelCategories(ViewModelListController):
	_name = "list:bc.class.model.categories"
	_view_name = "bc.class.model.categories/list"
	_description = "Category Class Models"

class ViewModelFormModalBcClassModelCategories(ViewModelFormModalController):
	_name = "form.modal:bc.class.model.categories"
	_view_name = "bc.class.model.categories/form.modal"
	_description = "Category Class Models"

class ViewModelFormBcClassModelCategories(ViewModelFormController):
	_name = "form:bc.class.model.categories"
	_view_name = "bc.class.model.categories/form"
	_description = "Category Class Models"
