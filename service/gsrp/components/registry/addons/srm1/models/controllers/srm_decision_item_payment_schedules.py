from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.decision.item.payment.schedules"
	_view_name = "srm.decision.item.payment.schedules/find"
	_description = "Decision Item Payment Schedules"

class ViewModelO2MFormSrmDecisionItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.item.payment.schedules"
	_view_name = "srm.decision.item.payment.schedules/o2m-form"
	_description = "Decision Item Payment Schedules"

class ViewModelO2MListSrmDecisionItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.item.payment.schedules"
	_view_name = "srm.decision.item.payment.schedules/o2m-list"
	_description = "Decision Item Payment Schedules"
