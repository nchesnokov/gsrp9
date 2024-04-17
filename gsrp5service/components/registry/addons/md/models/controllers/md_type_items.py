from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdTypeItems(ViewModelSearchController):
	_name = "search:md.type.items"
	_view_name = "md.type.items/search"
	_description = "Type Of Items"

class ViewModelFindMdTypeItems(ViewModelFindController):
	_name = "find:md.type.items"
	_view_name = "md.type.items/find"
	_description = "Type Of Items"

class ViewModelListMdTypeItems(ViewModelListController):
	_name = "list:md.type.items"
	_view_name = "md.type.items/list"
	_description = "Type Of Items"

class ViewModelFormModalMdTypeItems(ViewModelFormModalController):
	_name = "form.modal:md.type.items"
	_view_name = "md.type.items/form.modal"
	_description = "Type Of Items"

class ViewModelFormMdTypeItems(ViewModelFormController):
	_name = "form:md.type.items"
	_view_name = "md.type.items/form"
	_description = "Type Of Items"
