from orm import fields
from orm.model import Model

class wkf_locations(Model):
	_name = 'wkf.locations'
	_description = 'General Model WKF Location'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('supplier', 'Vendor Location'),
        ('view', 'View'),
        ('internal', 'Internal Location'),
        ('customer', 'Customer Location'),
        ('inventory', 'Inventory Loss'),
        ('procurement', 'Procurement'),
        ('production', 'Production'),
        ('transit', 'Transit Location')]),
	'name': fields.varchar(label = 'Name'),
	'parent_id': fields.many2one(label = 'Parent',obj='wkf.locations'),
	'childs_id': fields.one2many(label='Location',obj='wkf.locations',rel='parent_id'),
	'note': fields.text('Note')}

wkf_locations()

class wkf_workplace_categories(Model):
	_name = 'wkf.workplice.categories'
	_description = 'General Workflow Workplice Category'
	_columns = {
	'name': fields.varchar(label = 'Category'),
	'parent_id': fields.many2one(label='Parent',obj='wkf.workplice.categories'),
	'childs_id': fields.one2many(label='Childs',obj='wkf.workplice.categories',rel='parent_id'),
	'note': fields.text(label = 'Note')
	}

wkf_workplace_categories()

class wkf_workplaces(Model):
	_name = 'wkf.workplace'
	_description = 'General Workflow Workplaces'
	_columns = {
	'name': fields.varchar(label = 'Workplace'),
	'category_id': fields.many2one(label='Category',obj='wkf.workplice.categories'),
	'location_id': fields.many2one(label='Location',obj='wkf.locations'),
	'inactive': fields.boolean(label='Inactive'),
	'note': fields.text('Note')
	}

wkf_workplaces()

class wkf_element_categories(Model):
	_name = 'wkf.element.categories'
	_description = 'General Workflow Element Category'
	_columns = {
	'name': fields.varchar(label = 'Category'),
	'parent_id': fields.many2one(label='Parent',obj='wkf.element.categories'),
	'childs_id': fields.one2many(label='Childs',obj='wkf.element.categories',rel='parent_id'),
	'note': fields.text(label = 'Note')
	}

wkf_element_categories()


class wkf_elements(Model):
	_name = 'wkf.elements'
	_description = 'General Workflow Element'
	_columns = {
	'name': fields.varchar(label = 'Element'),
	'wkf_element_category_id': fields.many2one(label='Category',obj='wkf.element.categories'),
	'etype': fields.selection(label='Type',selections=[('R','Route'),('P','Phase'),('T','Task'),('S','Stage'),('W','Workflow'),('I','Inode'),('C','Check'),('D','Deduction'),('A','Action'),('?','Multipleхor'),('|','Or'),('&','And'),('!','Not'),('^','Xor'),('#','Selector'),(';','Terminator')]),
	'parent_id': fields.many2one(label='Parent',obj='wkf.elements'),
	'childs_id': fields.one2many(label='Childs',obj='wkf.elements',rel='parent_id'),
	'value': fields.boolean(label='Value',compute='_calculate_value'),
	'note': fields.text(label = 'Note')
	}

	def _calculate_value(self,cr,pool,uid,item,context):
		if item['etype'] == '&':
			res = list(set(map(lambda x: x['value'],pool.get(self._name).select(cr,pool,uid, ['value'],[('parent_id','=',item['parent_id'])],context))))
			return len(res) == 1 and res[0] or len(res) == 2 and False
		elif item['etype'] == '|':
			res = list(set(map(lambda x: x['value'],pool.get(self._name).select(cr,pool,uid, ['value'],[('parent_id','=',item['parent_id'])],context))))
			return len(res) == 1 and res[0] or len(res) == 2 and True
		elif item['etype'] == '!':
			res = list(set(map(lambda x: x['value'],pool.get(self._name).select(cr,pool,uid, ['value'],[('parent_id','=',item['parent_id'])],context,limit=1))))
			return not res[0]
		elif item['etype'] == '^':
			res = list(set(map(lambda x: x['value'],pool.get(self._name).select(cr,pool,uid, ['value'],[('parent_id','=',item['parent_id'])],context,limit=2))))
			return res[0] and res[1] or not res[0] and not res[1]
		
wkf_elements()

class wkf_routes(Model):
	_name = 'wkf.routes'
	_description = 'General Workflow Routes'
	_columns = {
	'name': fields.varchar(label = 'Route'),
	'element_id': fields.many2one(label='Element',obj='wkf.elements',domain=[('etype','=','R')]),
	'inactive': fields.boolean(label='Inactive'),
	'note': fields.text(label = 'Note')
	}

	_default = {
	
	}

wkf_routes()

class wkf_jobs(Model):
	_name = 'wkf.jobs'
	_description = 'General Workflow Jobs'
	_columns = {
	'name': fields.varchar(label = 'Job'),
	'parent_id': fields.many2one(label='Parent',obj='wkf.jobs'),
	'childs_id': fields.one2many(label='Childs',obj='wkf.jobs',rel='parent_id'),
	'start_date': fields.datetime(label='Start Date',timezone=True),
	'end_date': fields.datetime(label='End Date',timezone=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('started','Started'),('holded','holded'),('approved','Approved'),('inprocess','In Process'),('endded','Ended'),('closed','Closed')]),
	'department_id': fields.many2one(label='Department',obj='hcm.department'),
	'employee_id': fields.related(label='Executer',obj='hcm.employees',relatedy=['department_id']),
	'history': fields.one2many(label='History',obj='wkf.job.history',rel='job_id',readonly=True),
	'note': fields.text(label = 'Note')
	}
	
	_default = {
	'state': 'draft'
	}

wkf_jobs()

class wkf_job_history(Model):
	_name = 'wkf.job.history'
	_description = 'General Workflow History Job'
	_columns = {
	'job_id': fields.many2one(label='Job',obj='wkf.jobs',readonly=True),
	'ts': fields.datetime(label='Timestamp',timezone=True,readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('started','Started'),('holded','holded'),('approved','Approved'),('inprocess','In Process'),('endded','Ended'),('closed','Closed')],readonly=True),
	'department_id': fields.many2one(label='Department',obj='hcm.department',readonly=True),
	'employee_id': fields.related(label='Executer',obj='hcm.employees',relatedy='department_id',readonly=True),
	'note': fields.text(label = 'Note',readonly=True)
	}

wkf_job_history()

