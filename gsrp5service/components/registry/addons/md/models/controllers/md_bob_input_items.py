from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMdBobInputItems(ViewModelFindController):
	_name = "find:md.bob.input.items"
	_view_name = "md.bob.input.items/find"
	_description = "BoB Input items"

class ViewModelO2MFormMdBobInputItems(ViewModelO2MFormController):
	_name = "o2m-form:md.bob.input.items"
	_view_name = "md.bob.input.items/o2m-form"
	_description = "BoB Input items"

class ViewModelO2MListMdBobInputItems(ViewModelO2MListController):
	_name = "o2m-list:md.bob.input.items"
	_view_name = "md.bob.input.items/o2m-list"
	_description = "BoB Input items"
