from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponsePaymentSchedules(ViewModelFindController):
	_name = "find:srm.response.payment.schedules"
	_view_name = "srm.response.payment.schedules/find"
	_description = "SRM Response Payment Schedules"

class ViewModelO2MFormSrmResponsePaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.payment.schedules"
	_view_name = "srm.response.payment.schedules/o2m-form"
	_description = "SRM Response Payment Schedules"

class ViewModelO2MListSrmResponsePaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.response.payment.schedules"
	_view_name = "srm.response.payment.schedules/o2m-list"
	_description = "SRM Response Payment Schedules"
