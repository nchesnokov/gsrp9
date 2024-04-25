from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindStStockProductQuantites(ViewModelFindController):
	_name = "find:st.stock.product.quantites"
	_view_name = "st.stock.product.quantites/find"
	_description = "Stock Product Quantity"

class ViewModelO2MFormStStockProductQuantites(ViewModelO2MFormController):
	_name = "o2m-form:st.stock.product.quantites"
	_view_name = "st.stock.product.quantites/o2m-form"
	_description = "Stock Product Quantity"

class ViewModelO2MListStStockProductQuantites(ViewModelO2MListController):
	_name = "o2m-list:st.stock.product.quantites"
	_view_name = "st.stock.product.quantites/o2m-list"
	_description = "Stock Product Quantity"
