from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.response.item.payment.schedules"
	_view_name = "srm.response.item.payment.schedules/find"
	_description = "Response Item Payment Schedules"

class ViewModelO2MFormSrmResponseItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.item.payment.schedules"
	_view_name = "srm.response.item.payment.schedules/o2m-form"
	_description = "Response Item Payment Schedules"

class ViewModelO2MListSrmResponseItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.response.item.payment.schedules"
	_view_name = "srm.response.item.payment.schedules/o2m-list"
	_description = "Response Item Payment Schedules"
