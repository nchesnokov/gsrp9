from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferPaymentSchedules(ViewModelFindController):
	_name = "find:srm.offer.payment.schedules"
	_view_name = "srm.offer.payment.schedules/find"
	_description = "SRM Offer Payment Schedules"

class ViewModelO2MFormSrmOfferPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.payment.schedules"
	_view_name = "srm.offer.payment.schedules/o2m-form"
	_description = "SRM Offer Payment Schedules"

class ViewModelO2MListSrmOfferPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.payment.schedules"
	_view_name = "srm.offer.payment.schedules/o2m-list"
	_description = "SRM Offer Payment Schedules"
