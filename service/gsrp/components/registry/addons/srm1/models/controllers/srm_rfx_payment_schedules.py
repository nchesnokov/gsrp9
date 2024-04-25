from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxPaymentSchedules(ViewModelFindController):
	_name = "find:srm.rfx.payment.schedules"
	_view_name = "srm.rfx.payment.schedules/find"
	_description = "SRM RFX Payment Schedules"

class ViewModelO2MFormSrmRfxPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.payment.schedules"
	_view_name = "srm.rfx.payment.schedules/o2m-form"
	_description = "SRM RFX Payment Schedules"

class ViewModelO2MListSrmRfxPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.payment.schedules"
	_view_name = "srm.rfx.payment.schedules/o2m-list"
	_description = "SRM RFX Payment Schedules"
