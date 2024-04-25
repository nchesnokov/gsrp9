from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.part.item.payment.schedules"
	_view_name = "srm.part.item.payment.schedules/find"
	_description = "Part Item Payment Schedules"

class ViewModelO2MFormSrmPartItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.item.payment.schedules"
	_view_name = "srm.part.item.payment.schedules/o2m-form"
	_description = "Part Item Payment Schedules"

class ViewModelO2MListSrmPartItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.part.item.payment.schedules"
	_view_name = "srm.part.item.payment.schedules/o2m-list"
	_description = "Part Item Payment Schedules"
