from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchI18NRuMdOkei(ViewModelSearchController):
	_name = "search:i18n.ru.md.okei"
	_view_name = "i18n.ru.md.okei/search"
	_description = "Classifiers OKEI"

class ViewModelFindI18NRuMdOkei(ViewModelFindController):
	_name = "find:i18n.ru.md.okei"
	_view_name = "i18n.ru.md.okei/find"
	_description = "Classifiers OKEI"

class ViewModelListI18NRuMdOkei(ViewModelListController):
	_name = "list:i18n.ru.md.okei"
	_view_name = "i18n.ru.md.okei/list"
	_description = "Classifiers OKEI"

class ViewModelFormModalI18NRuMdOkei(ViewModelFormModalController):
	_name = "form.modal:i18n.ru.md.okei"
	_view_name = "i18n.ru.md.okei/form.modal"
	_description = "Classifiers OKEI"

class ViewModelFormI18NRuMdOkei(ViewModelFormController):
	_name = "form:i18n.ru.md.okei"
	_view_name = "i18n.ru.md.okei/form"
	_description = "Classifiers OKEI"
