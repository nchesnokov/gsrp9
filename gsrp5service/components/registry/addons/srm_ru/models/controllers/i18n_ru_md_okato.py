from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchI18NRuMdOkato(ViewModelSearchController):
	_name = "search:i18n.ru.md.okato"
	_view_name = "i18n.ru.md.okato/search"
	_description = "Classifiers OKATO"

class ViewModelFindI18NRuMdOkato(ViewModelFindController):
	_name = "find:i18n.ru.md.okato"
	_view_name = "i18n.ru.md.okato/find"
	_description = "Classifiers OKATO"

class ViewModelListI18NRuMdOkato(ViewModelListController):
	_name = "list:i18n.ru.md.okato"
	_view_name = "i18n.ru.md.okato/list"
	_description = "Classifiers OKATO"

class ViewModelFormModalI18NRuMdOkato(ViewModelFormModalController):
	_name = "form.modal:i18n.ru.md.okato"
	_view_name = "i18n.ru.md.okato/form.modal"
	_description = "Classifiers OKATO"

class ViewModelFormI18NRuMdOkato(ViewModelFormController):
	_name = "form:i18n.ru.md.okato"
	_view_name = "i18n.ru.md.okato/form"
	_description = "Classifiers OKATO"
