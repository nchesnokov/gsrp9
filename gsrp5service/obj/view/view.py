import os
import sys
import time
import logging
from functools import reduce
from .metaobjects import MetaObjects
from tools.translations import trlocal as _
#from . import mm
#from .mm import orm_exception
#from .mm import Access

_logger = logging.getLogger(__name__)


class View(object, metaclass = MetaObjects):
	_name = None
	_description = None

class ViewInherit(object, metaclass = MetaObjects):
	_name = None

class ViewModel(View):
	_model = None
	_columns = []

class ViewModelInherit(ViewInherit):
	_model = None

class ViewModelCalendar(ViewModel):
	_view_type = 'ModelCalendar'

class ViewModelForm(ViewModel):
	_view_type = 'ModelForm'

class ViewModelFormModal(ViewModel):
	_view_type = 'ModelFormModal'

class ViewModelFind(ViewModel):
	_view_type = 'ModelFind'

class ViewModelFlow(ViewModel):
	_view_type = 'ModelFlow'

class ViewModelGantt(ViewModel):
	_view_type = 'ModelGantt'

class ViewModelGeo(ViewModel):
	_view_type = 'ModelGeo'

class ViewModelGraph(ViewModel):
	_view_type = 'ModelGraph'

class ViewModelKanban(ViewModel):
	_view_type = 'ModelKanban'

class ViewModelList(ViewModel):
	_view_type = 'ModelList'

class ViewModelM2MList(ViewModel):
	_view_type = 'ModelM2MList'

class ViewModelMdx(ViewModel):
	_view_type = 'ModelMdx'

class ViewModelSearch(ViewModel):
	_view_type = 'ModelSearch'

class ViewModelSchedule(ViewModel):
	_view_type = 'ModelSchedule'

class ViewModelTree(ViewModel):
	_view_type = 'ModelTree'

