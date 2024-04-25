from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleChannelCategories(ViewModelSearchController):
	_name = "search:sale.channel.categories"
	_view_name = "sale.channel.categories/search"
	_description = "Categories Sale Chanel"

class ViewModelFindSaleChannelCategories(ViewModelFindController):
	_name = "find:sale.channel.categories"
	_view_name = "sale.channel.categories/find"
	_description = "Categories Sale Chanel"

class ViewModelListSaleChannelCategories(ViewModelListController):
	_name = "list:sale.channel.categories"
	_view_name = "sale.channel.categories/list"
	_description = "Categories Sale Chanel"

class ViewModelFormModalSaleChannelCategories(ViewModelFormModalController):
	_name = "form.modal:sale.channel.categories"
	_view_name = "sale.channel.categories/form.modal"
	_description = "Categories Sale Chanel"

class ViewModelFormSaleChannelCategories(ViewModelFormController):
	_name = "form:sale.channel.categories"
	_view_name = "sale.channel.categories/form"
	_description = "Categories Sale Chanel"

class ViewModelTreeSaleChannelCategories(ViewModelTreeController):
	_name = "tree:sale.channel.categories"
	_view_name = "sale.channel.categories/tree"
	_description = "Categories Sale Chanel"
