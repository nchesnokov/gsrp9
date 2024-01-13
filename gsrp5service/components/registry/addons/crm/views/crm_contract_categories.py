from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelTree
from gsrp5service.obj.view import ViewModelO2MTree
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmContractCategories(ViewModelSearch):
	_name = "model.search.crm.contract.categories"
	_model = "crm.contract.categories"
	_description = "Category Contract"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelFindCrmContractCategories(ViewModelFind):
	_name = "model.find.crm.contract.categories"
	_model = "crm.contract.categories"
	_description = "Category Contract"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MFormCrmContractCategories(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.categories"
	_model = "crm.contract.categories"
	_description = "Category Contract"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'orders', 'note']

class ViewModelTreeCrmContractCategories(ViewModelTree):
	_name = "model.tree.crm.contract.categories"
	_model = "crm.contract.categories"
	_description = "Category Contract"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MTreeCrmContractCategories(ViewModelO2MTree):
	_name = "model.o2mtree.crm.contract.categories"
	_model = "crm.contract.categories"
	_description = "Category Contract"
	_columns = ['name', 'parent_id', 'fullname']

class ViewModelO2MListCrmContractCategories(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.categories"
	_model = "crm.contract.categories"
	_description = "Category Contract"
	_columns = ['name', 'parent_id', 'childs_id', 'fullname', 'orders']
