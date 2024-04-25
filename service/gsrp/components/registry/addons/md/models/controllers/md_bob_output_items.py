from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdBobOutputItems(ViewModelFindController):
	_name = "find:md.bob.output.items"
	_view_name = "md.bob.output.items/find"
	_description = "BoB Output items"

class ViewModelO2MFormMdBobOutputItems(ViewModelO2MFormController):
	_name = "o2m-form:md.bob.output.items"
	_view_name = "md.bob.output.items/o2m-form"
	_description = "BoB Output items"

class ViewModelO2MListMdBobOutputItems(ViewModelO2MListController):
	_name = "o2m-list:md.bob.output.items"
	_view_name = "md.bob.output.items/o2m-list"
	_description = "BoB Output items"
