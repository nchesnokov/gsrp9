from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandPaymentSchedules(ViewModelFindController):
	_name = "find:srm.demand.payment.schedules"
	_view_name = "srm.demand.payment.schedules/find"
	_description = "SRM Demand Payment Schedules"

class ViewModelO2MFormSrmDemandPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.payment.schedules"
	_view_name = "srm.demand.payment.schedules/o2m-form"
	_description = "SRM Demand Payment Schedules"

class ViewModelO2MListSrmDemandPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.payment.schedules"
	_view_name = "srm.demand.payment.schedules/o2m-list"
	_description = "SRM Demand Payment Schedules"
