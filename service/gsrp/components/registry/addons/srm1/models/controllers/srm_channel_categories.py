from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmChannelCategories(ViewModelSearchController):
	_name = "search:srm.channel.categories"
	_view_name = "srm.channel.categories/search"
	_description = "Categories SRM Chanel"

class ViewModelFindSrmChannelCategories(ViewModelFindController):
	_name = "find:srm.channel.categories"
	_view_name = "srm.channel.categories/find"
	_description = "Categories SRM Chanel"

class ViewModelListSrmChannelCategories(ViewModelListController):
	_name = "list:srm.channel.categories"
	_view_name = "srm.channel.categories/list"
	_description = "Categories SRM Chanel"

class ViewModelFormModalSrmChannelCategories(ViewModelFormModalController):
	_name = "form.modal:srm.channel.categories"
	_view_name = "srm.channel.categories/form.modal"
	_description = "Categories SRM Chanel"

class ViewModelFormSrmChannelCategories(ViewModelFormController):
	_name = "form:srm.channel.categories"
	_view_name = "srm.channel.categories/form"
	_description = "Categories SRM Chanel"

class ViewModelTreeSrmChannelCategories(ViewModelTreeController):
	_name = "tree:srm.channel.categories"
	_view_name = "srm.channel.categories/tree"
	_description = "Categories SRM Chanel"
