from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMdCategoryProduct(ViewModelSearchController):
	_name = "search:md.category.product"
	_view_name = "md.category.product/search"
	_description = "Category Product"

class ViewModelFindMdCategoryProduct(ViewModelFindController):
	_name = "find:md.category.product"
	_view_name = "md.category.product/find"
	_description = "Category Product"

class ViewModelListMdCategoryProduct(ViewModelListController):
	_name = "list:md.category.product"
	_view_name = "md.category.product/list"
	_description = "Category Product"

class ViewModelFormModalMdCategoryProduct(ViewModelFormModalController):
	_name = "form.modal:md.category.product"
	_view_name = "md.category.product/form.modal"
	_description = "Category Product"

class ViewModelFormMdCategoryProduct(ViewModelFormController):
	_name = "form:md.category.product"
	_view_name = "md.category.product/form"
	_description = "Category Product"

class ViewModelTreeMdCategoryProduct(ViewModelTreeController):
	_name = "tree:md.category.product"
	_view_name = "md.category.product/tree"
	_description = "Category Product"
