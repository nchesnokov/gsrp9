from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMdCategoryLanguage(ViewModelSearchController):
	_name = "search:md.category.language"
	_view_name = "md.category.language/search"
	_description = "Category Language"

class ViewModelFindMdCategoryLanguage(ViewModelFindController):
	_name = "find:md.category.language"
	_view_name = "md.category.language/find"
	_description = "Category Language"

class ViewModelListMdCategoryLanguage(ViewModelListController):
	_name = "list:md.category.language"
	_view_name = "md.category.language/list"
	_description = "Category Language"

class ViewModelFormModalMdCategoryLanguage(ViewModelFormModalController):
	_name = "form.modal:md.category.language"
	_view_name = "md.category.language/form.modal"
	_description = "Category Language"

class ViewModelFormMdCategoryLanguage(ViewModelFormController):
	_name = "form:md.category.language"
	_view_name = "md.category.language/form"
	_description = "Category Language"

class ViewModelTreeMdCategoryLanguage(ViewModelTreeController):
	_name = "tree:md.category.language"
	_view_name = "md.category.language/tree"
	_description = "Category Language"
