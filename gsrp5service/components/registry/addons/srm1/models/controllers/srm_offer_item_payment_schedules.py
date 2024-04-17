from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.offer.item.payment.schedules"
	_view_name = "srm.offer.item.payment.schedules/find"
	_description = "Offer Item Payment Schedules"

class ViewModelO2MFormSrmOfferItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.item.payment.schedules"
	_view_name = "srm.offer.item.payment.schedules/o2m-form"
	_description = "Offer Item Payment Schedules"

class ViewModelO2MListSrmOfferItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.item.payment.schedules"
	_view_name = "srm.offer.item.payment.schedules/o2m-list"
	_description = "Offer Item Payment Schedules"
