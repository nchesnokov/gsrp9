from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoceItemDeliverySchedules(ViewModelFindController):
	_name = "find:purchase.invoce.item.delivery.schedules"
	_view_name = "purchase.invoce.item.delivery.schedules/find"
	_description = "Purchase Invoice Item Delivery Schedules"

class ViewModelO2MFormPurchaseInvoceItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoce.item.delivery.schedules"
	_view_name = "purchase.invoce.item.delivery.schedules/o2m-form"
	_description = "Purchase Invoice Item Delivery Schedules"

class ViewModelO2MListPurchaseInvoceItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoce.item.delivery.schedules"
	_view_name = "purchase.invoce.item.delivery.schedules/o2m-list"
	_description = "Purchase Invoice Item Delivery Schedules"
