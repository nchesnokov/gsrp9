from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMdGroupQuantity(ViewModelSearchController):
	_name = "search:md.group.quantity"
	_view_name = "md.group.quantity/search"
	_description = "Group Quantity"

class ViewModelFindMdGroupQuantity(ViewModelFindController):
	_name = "find:md.group.quantity"
	_view_name = "md.group.quantity/find"
	_description = "Group Quantity"

class ViewModelListMdGroupQuantity(ViewModelListController):
	_name = "list:md.group.quantity"
	_view_name = "md.group.quantity/list"
	_description = "Group Quantity"

class ViewModelFormModalMdGroupQuantity(ViewModelFormModalController):
	_name = "form.modal:md.group.quantity"
	_view_name = "md.group.quantity/form.modal"
	_description = "Group Quantity"

class ViewModelFormMdGroupQuantity(ViewModelFormController):
	_name = "form:md.group.quantity"
	_view_name = "md.group.quantity/form"
	_description = "Group Quantity"

class ViewModelTreeMdGroupQuantity(ViewModelTreeController):
	_name = "tree:md.group.quantity"
	_view_name = "md.group.quantity/tree"
	_description = "Group Quantity"
