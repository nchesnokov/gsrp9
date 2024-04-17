from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmChannelCategories(ViewModelSearchController):
	_name = "search:crm.channel.categories"
	_view_name = "crm.channel.categories/search"
	_description = "Categories CRM Chanel"

class ViewModelFindCrmChannelCategories(ViewModelFindController):
	_name = "find:crm.channel.categories"
	_view_name = "crm.channel.categories/find"
	_description = "Categories CRM Chanel"

class ViewModelListCrmChannelCategories(ViewModelListController):
	_name = "list:crm.channel.categories"
	_view_name = "crm.channel.categories/list"
	_description = "Categories CRM Chanel"

class ViewModelFormModalCrmChannelCategories(ViewModelFormModalController):
	_name = "form.modal:crm.channel.categories"
	_view_name = "crm.channel.categories/form.modal"
	_description = "Categories CRM Chanel"

class ViewModelFormCrmChannelCategories(ViewModelFormController):
	_name = "form:crm.channel.categories"
	_view_name = "crm.channel.categories/form"
	_description = "Categories CRM Chanel"

class ViewModelTreeCrmChannelCategories(ViewModelTreeController):
	_name = "tree:crm.channel.categories"
	_view_name = "crm.channel.categories/tree"
	_description = "Categories CRM Chanel"
