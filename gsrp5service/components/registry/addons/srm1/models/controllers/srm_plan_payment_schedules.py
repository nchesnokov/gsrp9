from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanPaymentSchedules(ViewModelFindController):
	_name = "find:srm.plan.payment.schedules"
	_view_name = "srm.plan.payment.schedules/find"
	_description = "SRM Plan Payment Schedules"

class ViewModelO2MFormSrmPlanPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.payment.schedules"
	_view_name = "srm.plan.payment.schedules/o2m-form"
	_description = "SRM Plan Payment Schedules"

class ViewModelO2MListSrmPlanPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.payment.schedules"
	_view_name = "srm.plan.payment.schedules/o2m-list"
	_description = "SRM Plan Payment Schedules"
