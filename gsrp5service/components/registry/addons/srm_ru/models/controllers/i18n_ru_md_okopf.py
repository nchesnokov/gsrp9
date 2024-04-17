from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchI18NRuMdOkopf(ViewModelSearchController):
	_name = "search:i18n.ru.md.okopf"
	_view_name = "i18n.ru.md.okopf/search"
	_description = "Classifiers OKOPF"

class ViewModelFindI18NRuMdOkopf(ViewModelFindController):
	_name = "find:i18n.ru.md.okopf"
	_view_name = "i18n.ru.md.okopf/find"
	_description = "Classifiers OKOPF"

class ViewModelListI18NRuMdOkopf(ViewModelListController):
	_name = "list:i18n.ru.md.okopf"
	_view_name = "i18n.ru.md.okopf/list"
	_description = "Classifiers OKOPF"

class ViewModelFormModalI18NRuMdOkopf(ViewModelFormModalController):
	_name = "form.modal:i18n.ru.md.okopf"
	_view_name = "i18n.ru.md.okopf/form.modal"
	_description = "Classifiers OKOPF"

class ViewModelFormI18NRuMdOkopf(ViewModelFormController):
	_name = "form:i18n.ru.md.okopf"
	_view_name = "i18n.ru.md.okopf/form"
	_description = "Classifiers OKOPF"
