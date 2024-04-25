from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestPaymentSchedules(ViewModelFindController):
	_name = "find:srm.request.payment.schedules"
	_view_name = "srm.request.payment.schedules/find"
	_description = "SRM Request Payment Schedules"

class ViewModelO2MFormSrmRequestPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.payment.schedules"
	_view_name = "srm.request.payment.schedules/o2m-form"
	_description = "SRM Request Payment Schedules"

class ViewModelO2MListSrmRequestPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.request.payment.schedules"
	_view_name = "srm.request.payment.schedules/o2m-list"
	_description = "SRM Request Payment Schedules"
