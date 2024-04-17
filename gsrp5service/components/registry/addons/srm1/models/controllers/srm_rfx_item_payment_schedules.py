from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.rfx.item.payment.schedules"
	_view_name = "srm.rfx.item.payment.schedules/find"
	_description = "RFX Item Payment Schedules"

class ViewModelO2MFormSrmRfxItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.item.payment.schedules"
	_view_name = "srm.rfx.item.payment.schedules/o2m-form"
	_description = "RFX Item Payment Schedules"

class ViewModelO2MListSrmRfxItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.item.payment.schedules"
	_view_name = "srm.rfx.item.payment.schedules/o2m-list"
	_description = "RFX Item Payment Schedules"
