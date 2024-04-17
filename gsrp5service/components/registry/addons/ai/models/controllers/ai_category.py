from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchAiCategory(ViewModelSearchController):
	_name = "search:ai.category"
	_view_name = "ai.category/search"
	_description = "Artificial Intelligence Category"

class ViewModelFindAiCategory(ViewModelFindController):
	_name = "find:ai.category"
	_view_name = "ai.category/find"
	_description = "Artificial Intelligence Category"

class ViewModelListAiCategory(ViewModelListController):
	_name = "list:ai.category"
	_view_name = "ai.category/list"
	_description = "Artificial Intelligence Category"

class ViewModelFormModalAiCategory(ViewModelFormModalController):
	_name = "form.modal:ai.category"
	_view_name = "ai.category/form.modal"
	_description = "Artificial Intelligence Category"

class ViewModelFormAiCategory(ViewModelFormController):
	_name = "form:ai.category"
	_view_name = "ai.category/form"
	_description = "Artificial Intelligence Category"
