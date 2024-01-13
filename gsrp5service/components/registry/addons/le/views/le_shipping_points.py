from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchLeShippingPoints(ViewModelSearch):
	_name = "model.search.le.shipping.points"
	_model = "le.shipping.points"
	_description = "Shipping Points"
	_columns = ['company_id', 'ptype', 'name']

class ViewModelFindLeShippingPoints(ViewModelFind):
	_name = "model.find.le.shipping.points"
	_model = "le.shipping.points"
	_description = "Shipping Points"
	_columns = ['company_id', 'ptype', 'name']

class ViewModelListLeShippingPoints(ViewModelList):
	_name = "model.list.le.shipping.points"
	_model = "le.shipping.points"
	_description = "Shipping Points"
	_columns = ['company_id', 'ptype', 'name', 'places']

class ViewModelFormModalLeShippingPoints(ViewModelFormModal):
	_name = "model.form.modal.le.shipping.points"
	_model = "le.shipping.points"
	_description = "Shipping Points"
	_columns = ['company_id', 'ptype', 'name', 'places', 'note']

class ViewModelFormLeShippingPoints(ViewModelForm):
	_name = "model.form.le.shipping.points"
	_model = "le.shipping.points"
	_description = "Shipping Points"
	_columns = ['company_id', 'ptype', 'name', 'places', 'note']

class ViewModelO2MFormLeShippingPoints(ViewModelO2MForm):
	_name = "model.o2mform.le.shipping.points"
	_model = "le.shipping.points"
	_description = "Shipping Points"
	_columns = ['company_id', 'ptype', 'name', 'places', 'note']

class ViewModelO2MListLeShippingPoints(ViewModelO2MList):
	_name = "model.o2mlist.le.shipping.points"
	_model = "le.shipping.points"
	_description = "Shipping Points"
	_columns = ['company_id', 'ptype', 'name', 'places']
