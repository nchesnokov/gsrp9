from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjChannelCategories(ViewModelSearchController):
	_name = "search:prj.channel.categories"
	_view_name = "prj.channel.categories/search"
	_description = "Categories Project Chanel"

class ViewModelFindPrjChannelCategories(ViewModelFindController):
	_name = "find:prj.channel.categories"
	_view_name = "prj.channel.categories/find"
	_description = "Categories Project Chanel"

class ViewModelListPrjChannelCategories(ViewModelListController):
	_name = "list:prj.channel.categories"
	_view_name = "prj.channel.categories/list"
	_description = "Categories Project Chanel"

class ViewModelFormModalPrjChannelCategories(ViewModelFormModalController):
	_name = "form.modal:prj.channel.categories"
	_view_name = "prj.channel.categories/form.modal"
	_description = "Categories Project Chanel"

class ViewModelFormPrjChannelCategories(ViewModelFormController):
	_name = "form:prj.channel.categories"
	_view_name = "prj.channel.categories/form"
	_description = "Categories Project Chanel"

class ViewModelTreePrjChannelCategories(ViewModelTreeController):
	_name = "tree:prj.channel.categories"
	_view_name = "prj.channel.categories/tree"
	_description = "Categories Project Chanel"
