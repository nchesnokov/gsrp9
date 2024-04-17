from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdProductsTemplate(ViewModelSearchController):
	_name = "search:md.products.template"
	_view_name = "md.products.template/search"
	_description = "Product Template"

class ViewModelFindMdProductsTemplate(ViewModelFindController):
	_name = "find:md.products.template"
	_view_name = "md.products.template/find"
	_description = "Product Template"

class ViewModelListMdProductsTemplate(ViewModelListController):
	_name = "list:md.products.template"
	_view_name = "md.products.template/list"
	_description = "Product Template"

class ViewModelFormModalMdProductsTemplate(ViewModelFormModalController):
	_name = "form.modal:md.products.template"
	_view_name = "md.products.template/form.modal"
	_description = "Product Template"

class ViewModelFormMdProductsTemplate(ViewModelFormController):
	_name = "form:md.products.template"
	_view_name = "md.products.template/form"
	_description = "Product Template"
