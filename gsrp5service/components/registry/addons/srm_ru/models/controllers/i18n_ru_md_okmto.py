from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchI18NRuMdOkmto(ViewModelSearchController):
	_name = "search:i18n.ru.md.okmto"
	_view_name = "i18n.ru.md.okmto/search"
	_description = "Classifiers OKMTO"

class ViewModelFindI18NRuMdOkmto(ViewModelFindController):
	_name = "find:i18n.ru.md.okmto"
	_view_name = "i18n.ru.md.okmto/find"
	_description = "Classifiers OKMTO"

class ViewModelListI18NRuMdOkmto(ViewModelListController):
	_name = "list:i18n.ru.md.okmto"
	_view_name = "i18n.ru.md.okmto/list"
	_description = "Classifiers OKMTO"

class ViewModelFormModalI18NRuMdOkmto(ViewModelFormModalController):
	_name = "form.modal:i18n.ru.md.okmto"
	_view_name = "i18n.ru.md.okmto/form.modal"
	_description = "Classifiers OKMTO"

class ViewModelFormI18NRuMdOkmto(ViewModelFormController):
	_name = "form:i18n.ru.md.okmto"
	_view_name = "i18n.ru.md.okmto/form"
	_description = "Classifiers OKMTO"
