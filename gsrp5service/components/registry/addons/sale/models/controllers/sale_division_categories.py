from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleDivisionCategories(ViewModelSearchController):
	_name = "search:sale.division.categories"
	_view_name = "sale.division.categories/search"
	_description = "Categories Sale Division"

class ViewModelFindSaleDivisionCategories(ViewModelFindController):
	_name = "find:sale.division.categories"
	_view_name = "sale.division.categories/find"
	_description = "Categories Sale Division"

class ViewModelListSaleDivisionCategories(ViewModelListController):
	_name = "list:sale.division.categories"
	_view_name = "sale.division.categories/list"
	_description = "Categories Sale Division"

class ViewModelFormModalSaleDivisionCategories(ViewModelFormModalController):
	_name = "form.modal:sale.division.categories"
	_view_name = "sale.division.categories/form.modal"
	_description = "Categories Sale Division"

class ViewModelFormSaleDivisionCategories(ViewModelFormController):
	_name = "form:sale.division.categories"
	_view_name = "sale.division.categories/form"
	_description = "Categories Sale Division"

class ViewModelTreeSaleDivisionCategories(ViewModelTreeController):
	_name = "tree:sale.division.categories"
	_view_name = "sale.division.categories/tree"
	_description = "Categories Sale Division"
