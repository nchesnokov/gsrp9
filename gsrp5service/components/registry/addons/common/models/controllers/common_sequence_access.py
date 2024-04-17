from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCommonSequenceAccess(ViewModelFindController):
	_name = "find:common.sequence.access"
	_view_name = "common.sequence.access/find"
	_description = "Common Sequences"

class ViewModelO2MFormCommonSequenceAccess(ViewModelO2MFormController):
	_name = "o2m-form:common.sequence.access"
	_view_name = "common.sequence.access/o2m-form"
	_description = "Common Sequences"

class ViewModelO2MListCommonSequenceAccess(ViewModelO2MListController):
	_name = "o2m-list:common.sequence.access"
	_view_name = "common.sequence.access/o2m-list"
	_description = "Common Sequences"
