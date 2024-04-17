from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdMobs(ViewModelSearchController):
	_name = "search:md.mobs"
	_view_name = "md.mobs/search"
	_description = "Material of Bills"

class ViewModelFindMdMobs(ViewModelFindController):
	_name = "find:md.mobs"
	_view_name = "md.mobs/find"
	_description = "Material of Bills"

class ViewModelListMdMobs(ViewModelListController):
	_name = "list:md.mobs"
	_view_name = "md.mobs/list"
	_description = "Material of Bills"

class ViewModelFormModalMdMobs(ViewModelFormModalController):
	_name = "form.modal:md.mobs"
	_view_name = "md.mobs/form.modal"
	_description = "Material of Bills"

class ViewModelFormMdMobs(ViewModelFormController):
	_name = "form:md.mobs"
	_view_name = "md.mobs/form"
	_description = "Material of Bills"
