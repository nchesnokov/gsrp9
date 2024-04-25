from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdBoms(ViewModelSearchController):
	_name = "search:md.boms"
	_view_name = "md.boms/search"
	_description = "Bill of Material"

class ViewModelFindMdBoms(ViewModelFindController):
	_name = "find:md.boms"
	_view_name = "md.boms/find"
	_description = "Bill of Material"

class ViewModelListMdBoms(ViewModelListController):
	_name = "list:md.boms"
	_view_name = "md.boms/list"
	_description = "Bill of Material"

class ViewModelFormModalMdBoms(ViewModelFormModalController):
	_name = "form.modal:md.boms"
	_view_name = "md.boms/form.modal"
	_description = "Bill of Material"

class ViewModelFormMdBoms(ViewModelFormController):
	_name = "form:md.boms"
	_view_name = "md.boms/form"
	_description = "Bill of Material"
