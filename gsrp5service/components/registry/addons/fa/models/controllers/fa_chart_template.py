from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaChartTemplate(ViewModelSearchController):
	_name = "search:fa.chart.template"
	_view_name = "fa.chart.template/search"
	_description = "Genaral Model Templates for Account Chart"

class ViewModelFindFaChartTemplate(ViewModelFindController):
	_name = "find:fa.chart.template"
	_view_name = "fa.chart.template/find"
	_description = "Genaral Model Templates for Account Chart"

class ViewModelListFaChartTemplate(ViewModelListController):
	_name = "list:fa.chart.template"
	_view_name = "fa.chart.template/list"
	_description = "Genaral Model Templates for Account Chart"

class ViewModelFormModalFaChartTemplate(ViewModelFormModalController):
	_name = "form.modal:fa.chart.template"
	_view_name = "fa.chart.template/form.modal"
	_description = "Genaral Model Templates for Account Chart"

class ViewModelFormFaChartTemplate(ViewModelFormController):
	_name = "form:fa.chart.template"
	_view_name = "fa.chart.template/form"
	_description = "Genaral Model Templates for Account Chart"
