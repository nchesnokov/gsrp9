from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartPaymentSchedules(ViewModelFindController):
	_name = "find:srm.part.payment.schedules"
	_view_name = "srm.part.payment.schedules/find"
	_description = "SRM Part Payment Schedules"

class ViewModelO2MFormSrmPartPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.payment.schedules"
	_view_name = "srm.part.payment.schedules/o2m-form"
	_description = "SRM Part Payment Schedules"

class ViewModelO2MListSrmPartPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.part.payment.schedules"
	_view_name = "srm.part.payment.schedules/o2m-list"
	_description = "SRM Part Payment Schedules"
