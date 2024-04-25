from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchLeMdGroupFreightCargo(ViewModelSearch):
	_name = "model.search.le.md.group.freight.cargo"
	_model = "le.md.group.freight.cargo"
	_description = "Fleight Cargo Group"
	_columns = ['name', 'descr']

class ViewModelFindLeMdGroupFreightCargo(ViewModelFind):
	_name = "model.find.le.md.group.freight.cargo"
	_model = "le.md.group.freight.cargo"
	_description = "Fleight Cargo Group"
	_columns = ['name', 'descr']

class ViewModelListLeMdGroupFreightCargo(ViewModelList):
	_name = "model.list.le.md.group.freight.cargo"
	_model = "le.md.group.freight.cargo"
	_description = "Fleight Cargo Group"
	_columns = ['name', 'descr']

class ViewModelFormModalLeMdGroupFreightCargo(ViewModelFormModal):
	_name = "model.form.modal.le.md.group.freight.cargo"
	_model = "le.md.group.freight.cargo"
	_description = "Fleight Cargo Group"
	_columns = ['name', 'descr', 'note']

class ViewModelFormLeMdGroupFreightCargo(ViewModelForm):
	_name = "model.form.le.md.group.freight.cargo"
	_model = "le.md.group.freight.cargo"
	_description = "Fleight Cargo Group"
	_columns = ['name', 'descr', 'note']
