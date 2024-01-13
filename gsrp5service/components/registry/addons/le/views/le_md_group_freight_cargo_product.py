from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeMdGroupFreightCargoProduct(ViewModelFind):
	_name = "model.find.le.md.group.freight.cargo.product"
	_model = "le.md.group.freight.cargo.product"
	_description = "Fleight Cargo Group Product"
	_columns = ['product_id', 'group_freight_cargo_id']

class ViewModelListLeMdGroupFreightCargoProduct(ViewModelList):
	_name = "model.list.le.md.group.freight.cargo.product"
	_model = "le.md.group.freight.cargo.product"
	_description = "Fleight Cargo Group Product"
	_columns = ['product_id', 'group_freight_cargo_id']

class ViewModelFormModalLeMdGroupFreightCargoProduct(ViewModelFormModal):
	_name = "model.form.modal.le.md.group.freight.cargo.product"
	_model = "le.md.group.freight.cargo.product"
	_description = "Fleight Cargo Group Product"
	_columns = ['product_id', 'group_freight_cargo_id']

class ViewModelFormLeMdGroupFreightCargoProduct(ViewModelForm):
	_name = "model.form.le.md.group.freight.cargo.product"
	_model = "le.md.group.freight.cargo.product"
	_description = "Fleight Cargo Group Product"
	_columns = ['product_id', 'group_freight_cargo_id']

class ViewModelO2MFormLeMdGroupFreightCargoProduct(ViewModelO2MForm):
	_name = "model.o2mform.le.md.group.freight.cargo.product"
	_model = "le.md.group.freight.cargo.product"
	_description = "Fleight Cargo Group Product"
	_columns = ['product_id', 'group_freight_cargo_id']

class ViewModelO2MListLeMdGroupFreightCargoProduct(ViewModelO2MList):
	_name = "model.o2mlist.le.md.group.freight.cargo.product"
	_model = "le.md.group.freight.cargo.product"
	_description = "Fleight Cargo Group Product"
	_columns = ['product_id', 'group_freight_cargo_id']
