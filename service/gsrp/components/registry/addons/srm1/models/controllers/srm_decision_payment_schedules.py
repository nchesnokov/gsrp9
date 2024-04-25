from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionPaymentSchedules(ViewModelFindController):
	_name = "find:srm.decision.payment.schedules"
	_view_name = "srm.decision.payment.schedules/find"
	_description = "SRM Decision Payment Schedules"

class ViewModelO2MFormSrmDecisionPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.payment.schedules"
	_view_name = "srm.decision.payment.schedules/o2m-form"
	_description = "SRM Decision Payment Schedules"

class ViewModelO2MListSrmDecisionPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.payment.schedules"
	_view_name = "srm.decision.payment.schedules/o2m-list"
	_description = "SRM Decision Payment Schedules"
