from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPurchaseChannelCategories(ViewModelSearchController):
	_name = "search:purchase.channel.categories"
	_view_name = "purchase.channel.categories/search"
	_description = "Categories Purchase Chanel"

class ViewModelFindPurchaseChannelCategories(ViewModelFindController):
	_name = "find:purchase.channel.categories"
	_view_name = "purchase.channel.categories/find"
	_description = "Categories Purchase Chanel"

class ViewModelListPurchaseChannelCategories(ViewModelListController):
	_name = "list:purchase.channel.categories"
	_view_name = "purchase.channel.categories/list"
	_description = "Categories Purchase Chanel"

class ViewModelFormModalPurchaseChannelCategories(ViewModelFormModalController):
	_name = "form.modal:purchase.channel.categories"
	_view_name = "purchase.channel.categories/form.modal"
	_description = "Categories Purchase Chanel"

class ViewModelFormPurchaseChannelCategories(ViewModelFormController):
	_name = "form:purchase.channel.categories"
	_view_name = "purchase.channel.categories/form"
	_description = "Categories Purchase Chanel"

class ViewModelTreePurchaseChannelCategories(ViewModelTreeController):
	_name = "tree:purchase.channel.categories"
	_view_name = "purchase.channel.categories/tree"
	_description = "Categories Purchase Chanel"
