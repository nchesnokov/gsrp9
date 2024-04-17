from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.evolution.item.payment.schedules"
	_view_name = "srm.evolution.item.payment.schedules/find"
	_description = "Evolution Item Payment Schedules"

class ViewModelO2MFormSrmEvolutionItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.item.payment.schedules"
	_view_name = "srm.evolution.item.payment.schedules/o2m-form"
	_description = "Evolution Item Payment Schedules"

class ViewModelO2MListSrmEvolutionItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.item.payment.schedules"
	_view_name = "srm.evolution.item.payment.schedules/o2m-list"
	_description = "Evolution Item Payment Schedules"
