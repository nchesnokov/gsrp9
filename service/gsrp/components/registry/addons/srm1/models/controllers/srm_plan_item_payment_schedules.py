from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.plan.item.payment.schedules"
	_view_name = "srm.plan.item.payment.schedules/find"
	_description = "Plan Item Payment Schedules"

class ViewModelO2MFormSrmPlanItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.item.payment.schedules"
	_view_name = "srm.plan.item.payment.schedules/o2m-form"
	_description = "Plan Item Payment Schedules"

class ViewModelO2MListSrmPlanItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.item.payment.schedules"
	_view_name = "srm.plan.item.payment.schedules/o2m-list"
	_description = "Plan Item Payment Schedules"
