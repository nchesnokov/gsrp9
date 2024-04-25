from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMrpTexts(ViewModelSearchController):
	_name = "search:mrp.texts"
	_view_name = "mrp.texts/search"
	_description = "MRP Texts"

class ViewModelFindMrpTexts(ViewModelFindController):
	_name = "find:mrp.texts"
	_view_name = "mrp.texts/find"
	_description = "MRP Texts"

class ViewModelListMrpTexts(ViewModelListController):
	_name = "list:mrp.texts"
	_view_name = "mrp.texts/list"
	_description = "MRP Texts"

class ViewModelFormModalMrpTexts(ViewModelFormModalController):
	_name = "form.modal:mrp.texts"
	_view_name = "mrp.texts/form.modal"
	_description = "MRP Texts"

class ViewModelFormMrpTexts(ViewModelFormController):
	_name = "form:mrp.texts"
	_view_name = "mrp.texts/form"
	_description = "MRP Texts"
