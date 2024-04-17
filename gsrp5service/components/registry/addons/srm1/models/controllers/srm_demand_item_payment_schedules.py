from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.demand.item.payment.schedules"
	_view_name = "srm.demand.item.payment.schedules/find"
	_description = "Demand Item Payment Schedules"

class ViewModelO2MFormSrmDemandItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.item.payment.schedules"
	_view_name = "srm.demand.item.payment.schedules/o2m-form"
	_description = "Demand Item Payment Schedules"

class ViewModelO2MListSrmDemandItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.item.payment.schedules"
	_view_name = "srm.demand.item.payment.schedules/o2m-list"
	_description = "Demand Item Payment Schedules"
