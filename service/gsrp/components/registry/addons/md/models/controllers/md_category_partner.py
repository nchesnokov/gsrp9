from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMdCategoryPartner(ViewModelSearchController):
	_name = "search:md.category.partner"
	_view_name = "md.category.partner/search"
	_description = "Category Partner"

class ViewModelFindMdCategoryPartner(ViewModelFindController):
	_name = "find:md.category.partner"
	_view_name = "md.category.partner/find"
	_description = "Category Partner"

class ViewModelListMdCategoryPartner(ViewModelListController):
	_name = "list:md.category.partner"
	_view_name = "md.category.partner/list"
	_description = "Category Partner"

class ViewModelFormModalMdCategoryPartner(ViewModelFormModalController):
	_name = "form.modal:md.category.partner"
	_view_name = "md.category.partner/form.modal"
	_description = "Category Partner"

class ViewModelFormMdCategoryPartner(ViewModelFormController):
	_name = "form:md.category.partner"
	_view_name = "md.category.partner/form"
	_description = "Category Partner"

class ViewModelTreeMdCategoryPartner(ViewModelTreeController):
	_name = "tree:md.category.partner"
	_view_name = "md.category.partner/tree"
	_description = "Category Partner"
