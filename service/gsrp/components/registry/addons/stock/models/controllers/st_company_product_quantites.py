from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindStCompanyProductQuantites(ViewModelFindController):
	_name = "find:st.company.product.quantites"
	_view_name = "st.company.product.quantites/find"
	_description = "Company Product Quantity"

class ViewModelO2MFormStCompanyProductQuantites(ViewModelO2MFormController):
	_name = "o2m-form:st.company.product.quantites"
	_view_name = "st.company.product.quantites/o2m-form"
	_description = "Company Product Quantity"

class ViewModelO2MListStCompanyProductQuantites(ViewModelO2MListController):
	_name = "o2m-list:st.company.product.quantites"
	_view_name = "st.company.product.quantites/o2m-list"
	_description = "Company Product Quantity"
