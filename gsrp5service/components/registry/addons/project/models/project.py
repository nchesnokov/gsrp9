from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

class prj_resource(Model):
	_name = 'prj.resource'
	_description = 'Project Resource'
	_columns = {
	'name': fields.varchar(label = 'Resource',translate=True),
	'category_id': fields.many2one(label='Category',obj='prj.resource.category'),
	'cost': fields.numeric(label='Cost',size=(11,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'note': fields.text('Note')
	}

prj_resource()

class prj_bill(Model):
	_name = 'prj.bill'
	_description = 'Projects Bill'
	_columns = {
	'btype': fields.many2one(label='Type',obj='prj.bill.types',on_change='_on_change_btype', required = True),
	'name': fields.varchar(label = 'Bill', required = True),
	'company': fields.many2one(label='Company',obj='md.company', required = True),
	'fullname': fields.composite(label='Full Name', cols = ['company','btype','name'], translate = True,required = True),
	'category_id': fields.many2one(label='Category',obj='prj.bill.category'),
	'parent_id': fields.many2one(label='Parent',obj='prj.bill'),
	'childs_id': fields.one2many(label='Childs',obj='prj.bill',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'prj_type': fields.selection(label='Project Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'portfolios': fields.one2many(label='Portfolios',obj='prj.portfolio',rel='bill_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'prj_type':'project'
	}

prj_bill()

class prj_portfolio(Model):
	_name = 'prj.portfolio'
	_description = 'Projects Portfolio'
	_columns = {
	'bill_id': fields.many2one(label='Bill',obj='prj.bill'),
	'name': fields.varchar(label = 'Portfolio'),
	'category_id': fields.many2one(label='Category',obj='prj.portfolio.category'),
	'parent_id': fields.many2one(label='Parent',obj='prj.portfolio'),
	'childs_id': fields.one2many(label='Childs',obj='prj.portfolio',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'prj_type': fields.selection(label='Project Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'projects': fields.one2many(label='Projects',obj='prj.project',rel='portfolio_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'prj_type':'project'

	}

prj_portfolio()

class prj_project(Model):
	_name = 'prj.project'
	_description = 'Project'
	_columns = {
	'portfolio_id': fields.many2one(label='Portfolio',obj='prj.portfolio',rel='projects'),
	'name': fields.varchar(label = 'Project'),
	'category_id': fields.many2one(label='Category',obj='prj.prj.category'),
	'parent_id': fields.many2one(label='Parent',obj='prj.project'),
	'childs_id': fields.one2many(label='Childs',obj='prj.project',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'prj_type': fields.selection(label='Project Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'stages': fields.one2many(label='Stages',obj='prj.stage',rel='prj_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'prj_type':'project'
	}

prj_project()

class prj_stage(Model):
	_name = 'prj.stage'
	_description = 'Project Stage'
	_columns = {
	'prj_id': fields.many2one(label='Project',obj='prj.project', on_delete='c', on_update='c'),
	'name': fields.varchar(label = 'Stage'),
	'type': fields.selection(label='Type',selections=[('b','Begin'),('e','End'),('w','Work'),('s','Situtation')]),
	'parent_id': fields.many2one(label='Parent',obj='prj.stage'),
	'childs_id': fields.one2many(label='Childs',obj='prj.stage',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'prj_type': fields.selection(label='Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),	
	'state': fields.selection(label='Project State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'tasks': fields.one2many(label='Tasks',obj='prj.task',rel='stage_id'),
	'elements': fields.one2many(label='Elements',obj='prj.element',rel='stage_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'prj_type':'milestone'
	}

prj_stage()

class prj_task(Model):
	_name = 'prj.task'
	_description = 'Project Task'
	_columns = {
	'stage_id': fields.many2one(label='Stage',obj='prj.stage', on_delete='c', on_update='c',selectable=True,required=True),
	'name': fields.varchar(label = 'Task',translate=True),
	'category_id': fields.many2one(label='Category',obj='prj.task.category'),
	'parent_id': fields.many2one(label='Parent',obj='prj.task'),
	'childs_id': fields.one2many(label='Childs',obj='prj.task',rel='parent_id'),
	'start_date': fields.datetime(label='Start date',timezone=True,required=True),
	'end_date': fields.datetime(label='End date',timezone=True,required=True),
	'progress': fields.numeric(label='Progress',size=(5,2),check='progress <= 100.00'),
	'prj_type': fields.selection(label='Project Type',selections=[('project','Project'),('milestone','Milestone'),('task','Task')],readonly=True),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'resources': fields.one2many(label='Recources',obj='prj.task.resources',rel='task_id'),
	'note': fields.text('Note')
	}

	_default = {
		'state':'draft',
		'prj_type': 'task'
	}

prj_task()

class prj_element(Model):
	_name = 'prj.element'
	_description = 'Project Element'
	_columns = {
	'stage_id': fields.many2one(label='Stage',obj='prj.stage', on_delete='c', on_update='c', selectable=True, required=True),
	'name': fields.varchar(label = 'Element',translate=True),
	'parent_id': fields.many2one(label='Parent',obj='prj.element'),
	'childs_id': fields.one2many(label='Childs',obj='prj.element',rel='parent_id'),
	'products': fields.one2many(label='Products',obj='prj.element.products',rel='element_id'),
	'resources': fields.one2many(label='Resources',obj='prj.element.resources',rel='element_id'),
	'note': fields.text('Note')
	}

prj_element()

class prj_element_products(Model):
	_name = 'prj.element.products'
	_description = 'Project Element Products'
	_columns = {
	'element_id': fields.many2one(label='Element',obj='prj.element', on_delete='c', on_update='c',selectable=True,required=True),
	'product_id': fields.many2one(label = 'Product',obj='md.product'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'note': fields.text('Note')
	}

prj_element_products()

class prj_task_resources(Model):
	_name = 'prj.task.resources'
	_description = 'Project Task Resources'
	_columns = {
	'task_id': fields.many2one(label = 'Task',obj='prj.task', on_delete='c', on_update='c',required=True),
	'resource_id': fields.many2one(label = 'Resource',obj='prj.resource', on_delete='c', on_update='c',required=True),
	'quantiny': fields.integer(label='Job',required=True),
	'uom': fields.many2one(label='Unit Of Measure',obj='md.uom',domain=[('quantity_id','=','Time')])
	}

prj_task_resources()

class prj_element_resources(Model):
	_name = 'prj.element.resources'
	_description = 'Project Element Resources'
	_columns = {
	'element_id': fields.many2one(label = 'Element',obj='prj.element', on_delete='c', on_update='c',required=True),
	'resource_id': fields.many2one(label = 'Resource',obj='prj.resource', on_delete='c', on_update='c',required=True),
	'quantiny': fields.integer(label='Job',required=True),
	'uom': fields.many2one(label='Unit Of Measure',obj='md.uom',domain=[('quantity_id','=','Time')])
	}

prj_element_resources()

class md_prj_product(Model):
	_name = 'md.prj.product'
	_description = 'Project Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'vat': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('p','n'))]),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_prj_product()

class md_prj_product_inherit(ModelInherit):
	_name = 'md.prj.product.inherit'
	_description = 'Genaral Model Inherit For project Product'
	_inherit = {'md.product':{'_columns':['project']},'md.boms':{'_columns':['usage']}}
	_columns = {
		'project': fields.one2many(label='Project',obj='md.prj.product',rel='product_id'),
		'usage': fields.iProperty(selections=[('prj','Project')])
	}
	
md_prj_product_inherit()

class prj_units_md_company_inherit(ModelInherit):
	_name = 'prj.units.md.company.inherit'
	_description = 'Project Units Master Data Company Inherit'
	_inherit = {'md.company':{'_columns':['prj_units']}}
	_columns={
	'prj_units': fields.many2many(label='Project Units',obj='prj.units',rel='md_company_prj_unit_rel',id1='unit_id',id2='company_id'),
	}
