from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdMobItems(ViewModelFindController):
	_name = "find:md.mob.items"
	_view_name = "md.mob.items/find"
	_description = "MoB items"

class ViewModelO2MFormMdMobItems(ViewModelO2MFormController):
	_name = "o2m-form:md.mob.items"
	_view_name = "md.mob.items/o2m-form"
	_description = "MoB items"

class ViewModelO2MListMdMobItems(ViewModelO2MListController):
	_name = "o2m-list:md.mob.items"
	_view_name = "md.mob.items/o2m-list"
	_description = "MoB items"
