from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMdCategoryCountry(ViewModelSearchController):
	_name = "search:md.category.country"
	_view_name = "md.category.country/search"
	_description = "Category Country"

class ViewModelFindMdCategoryCountry(ViewModelFindController):
	_name = "find:md.category.country"
	_view_name = "md.category.country/find"
	_description = "Category Country"

class ViewModelListMdCategoryCountry(ViewModelListController):
	_name = "list:md.category.country"
	_view_name = "md.category.country/list"
	_description = "Category Country"

class ViewModelFormModalMdCategoryCountry(ViewModelFormModalController):
	_name = "form.modal:md.category.country"
	_view_name = "md.category.country/form.modal"
	_description = "Category Country"

class ViewModelFormMdCategoryCountry(ViewModelFormController):
	_name = "form:md.category.country"
	_view_name = "md.category.country/form"
	_description = "Category Country"

class ViewModelTreeMdCategoryCountry(ViewModelTreeController):
	_name = "tree:md.category.country"
	_view_name = "md.category.country/tree"
	_description = "Category Country"
