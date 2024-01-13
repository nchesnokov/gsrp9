from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchLeLoadingPlaces(ViewModelSearch):
	_name = "model.search.le.loading.places"
	_model = "le.loading.places"
	_description = "Loading Places"
	_columns = ['point_id', 'name']

class ViewModelFindLeLoadingPlaces(ViewModelFind):
	_name = "model.find.le.loading.places"
	_model = "le.loading.places"
	_description = "Loading Places"
	_columns = ['point_id', 'name']

class ViewModelListLeLoadingPlaces(ViewModelList):
	_name = "model.list.le.loading.places"
	_model = "le.loading.places"
	_description = "Loading Places"
	_columns = ['point_id', 'name']

class ViewModelFormModalLeLoadingPlaces(ViewModelFormModal):
	_name = "model.form.modal.le.loading.places"
	_model = "le.loading.places"
	_description = "Loading Places"
	_columns = ['point_id', 'name', 'note']

class ViewModelFormLeLoadingPlaces(ViewModelForm):
	_name = "model.form.le.loading.places"
	_model = "le.loading.places"
	_description = "Loading Places"
	_columns = ['point_id', 'name', 'note']

class ViewModelO2MFormLeLoadingPlaces(ViewModelO2MForm):
	_name = "model.o2mform.le.loading.places"
	_model = "le.loading.places"
	_description = "Loading Places"
	_columns = ['point_id', 'name', 'note']

class ViewModelO2MListLeLoadingPlaces(ViewModelO2MList):
	_name = "model.o2mlist.le.loading.places"
	_model = "le.loading.places"
	_description = "Loading Places"
	_columns = ['point_id', 'name']
