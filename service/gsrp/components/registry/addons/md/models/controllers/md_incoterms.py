from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdIncoterms(ViewModelSearchController):
	_name = "search:md.incoterms"
	_view_name = "md.incoterms/search"
	_description = "Incoterms"

class ViewModelFindMdIncoterms(ViewModelFindController):
	_name = "find:md.incoterms"
	_view_name = "md.incoterms/find"
	_description = "Incoterms"

class ViewModelListMdIncoterms(ViewModelListController):
	_name = "list:md.incoterms"
	_view_name = "md.incoterms/list"
	_description = "Incoterms"

class ViewModelFormModalMdIncoterms(ViewModelFormModalController):
	_name = "form.modal:md.incoterms"
	_view_name = "md.incoterms/form.modal"
	_description = "Incoterms"

class ViewModelFormMdIncoterms(ViewModelFormController):
	_name = "form:md.incoterms"
	_view_name = "md.incoterms/form"
	_description = "Incoterms"
