from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionPaymentSchedules(ViewModelFindController):
	_name = "find:srm.evolution.payment.schedules"
	_view_name = "srm.evolution.payment.schedules/find"
	_description = "SRM Evolution Payment Schedules"

class ViewModelO2MFormSrmEvolutionPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.payment.schedules"
	_view_name = "srm.evolution.payment.schedules/o2m-form"
	_description = "SRM Evolution Payment Schedules"

class ViewModelO2MListSrmEvolutionPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.payment.schedules"
	_view_name = "srm.evolution.payment.schedules/o2m-list"
	_description = "SRM Evolution Payment Schedules"
