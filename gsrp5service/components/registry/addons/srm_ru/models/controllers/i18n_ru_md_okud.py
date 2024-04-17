from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchI18NRuMdOkud(ViewModelSearchController):
	_name = "search:i18n.ru.md.okud"
	_view_name = "i18n.ru.md.okud/search"
	_description = "Classifiers OKUD"

class ViewModelFindI18NRuMdOkud(ViewModelFindController):
	_name = "find:i18n.ru.md.okud"
	_view_name = "i18n.ru.md.okud/find"
	_description = "Classifiers OKUD"

class ViewModelListI18NRuMdOkud(ViewModelListController):
	_name = "list:i18n.ru.md.okud"
	_view_name = "i18n.ru.md.okud/list"
	_description = "Classifiers OKUD"

class ViewModelFormModalI18NRuMdOkud(ViewModelFormModalController):
	_name = "form.modal:i18n.ru.md.okud"
	_view_name = "i18n.ru.md.okud/form.modal"
	_description = "Classifiers OKUD"

class ViewModelFormI18NRuMdOkud(ViewModelFormController):
	_name = "form:i18n.ru.md.okud"
	_view_name = "i18n.ru.md.okud/form"
	_description = "Classifiers OKUD"
