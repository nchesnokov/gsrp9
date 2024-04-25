from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.request.item.payment.schedules"
	_view_name = "srm.request.item.payment.schedules/find"
	_description = "Request Item Payment Schedules"

class ViewModelO2MFormSrmRequestItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.item.payment.schedules"
	_view_name = "srm.request.item.payment.schedules/o2m-form"
	_description = "Request Item Payment Schedules"

class ViewModelO2MListSrmRequestItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.request.item.payment.schedules"
	_view_name = "srm.request.item.payment.schedules/o2m-list"
	_description = "Request Item Payment Schedules"
