from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchI18NRuMdOkso(ViewModelSearchController):
	_name = "search:i18n.ru.md.okso"
	_view_name = "i18n.ru.md.okso/search"
	_description = "Classifiers OKSO"

class ViewModelFindI18NRuMdOkso(ViewModelFindController):
	_name = "find:i18n.ru.md.okso"
	_view_name = "i18n.ru.md.okso/find"
	_description = "Classifiers OKSO"

class ViewModelListI18NRuMdOkso(ViewModelListController):
	_name = "list:i18n.ru.md.okso"
	_view_name = "i18n.ru.md.okso/list"
	_description = "Classifiers OKSO"

class ViewModelFormModalI18NRuMdOkso(ViewModelFormModalController):
	_name = "form.modal:i18n.ru.md.okso"
	_view_name = "i18n.ru.md.okso/form.modal"
	_description = "Classifiers OKSO"

class ViewModelFormI18NRuMdOkso(ViewModelFormController):
	_name = "form:i18n.ru.md.okso"
	_view_name = "i18n.ru.md.okso/form"
	_description = "Classifiers OKSO"
