from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

class hcm_employee_categories(Model):

	_name = "hcm.employee.categories"
	_description = "Employee Category"
	_columns = {
	'name': fields.varchar(label="Employee Tag", required=True),
	'color': fields.integer(label='Color Index'),
	'employee_ids': fields.many2many(obj='hcm.employees', rel='hcm_employee_categories_rel', id2='emp_id', id1='category_id', label='Employees')}

hcm_employee_categories()

class hcm_department(Model):
	_name = "hcm.department"
	_description = "HR Department"
	_order_by = "fullname"
	_rec_name = 'complete_name'
	_full_name = 'fullname'
	_columns = {
	'company': fields.many2one(obj='md.company', label='Company'),
	'name': fields.varchar(label='Department Name', required=True),
	'parent_id': fields.many2one(obj='hcm.department', label='Parent Department'),
	'childs_id': fields.one2many(obj='hcm.department', rel='parent_id', label='Child Departments'),
	'fullname': fields.composite(label='Full Name', priority=1, translate = True,required = True, compute = '_compute_composite_tree'),
	'complete_name': fields.varchar(label='Complete Name', priority=2, translate = True,required = True, compute = '_compute_complete_name'),
	'manager_id':  fields.many2one(obj='hcm.employees', label='Manager'),
	'member_ids': fields.one2many(obj='hcm.employees', rel='department_id', label='Members'),
	'jobs_ids': fields.one2many(obj='hcm.job', rel='department_id', label='Jobs'),
	'note': fields.text(label='Note'),
	'color': fields.integer(label='Color Index'),
	'active': fields.boolean('Active')
	}

	def _compute_complete_name(self,item,context):
		if item['fullname'] and item['company'] and item['company']['name']:
			item['complete_name'] = item['company']['name'] + '/' + item['fullname']

	_default ={'active':True,'color':1}

hcm_department()

class hcm_job(Model):

	_name = "hcm.job"
	_description = "Job Position"
	_columns = {
	'name': fields.varchar(label='Job Position', required=True, size = 128, translate=True),
	'expected_employees': fields.integer(compute='_compute_employees', label='Total Forecasted Employees', store=True,
		help='Expected number of employees for this job position after new recruitment.'),
	'no_of_employee': fields.integer(compute='_compute_employees', label="Current Number of Employees", store=True,
		help='Number of employees currently occupying this job position.'),
	'no_of_recruitment': fields.integer(label='Expected New Employees',
		help='Number of new employees you expect to recruit.'),
	'no_of_hired_employee': fields.integer(label='Hired Employees', help='Number of hired employees for this job position during recruitment phase.'),
	'employee_ids': fields.one2many(obj='hcm.employees', rel='job_id', label='Employees'),
	'description':  fields.text(label='Job Description'),
	'requirements': fields.text(label='Requirements'),
	'department_id': fields.many2one(obj='hcm.department', label='Department'),
	'company_id': fields.many2one(obj='md.company', label='Company'),
	'state': fields.selection(selections=[('recruit', 'Recruitment in Progress'),('open', 'Not Recruiting')], label='Status', readonly=True, required=True, help="Set whether the recruitment process is open or closed for this job position.")
	}

	def _compute_employees(self, record,context = {}):
		return {'expected_employees':15}

	_sql_constraints = [('name_company_uniq', 'unique(name, company_id, department_id)', 'The name of the job position must be unique per department in company!'),]

	_default = {
		'state':'open'
	}

hcm_job()

class hcm_employees(Model):
	_name = 'hcm.employees'
	_description = 'Employees Humam Capital Managament'
	_rec_name='fullname'
	_order_by = 'fullname'
	_childs_id = 'child_ids'
	_class_model = 'B'
	_columns = {
	# resource and user
	# required on the resource, make sure required="True" set in the view
	'firstname': fields.varchar(label = 'First Name'),
	'lastname': fields.varchar(label = 'Last Name'),
	'middlename': fields.varchar(label = 'Middle Name'),
	'birthday': fields.date(label='Date of Birth'),
	'fullname': fields.composite(label='Full Name', cols = ['lastname','firstname','middlename','birthday'], translate = True,required = True, compute = '_compute_composite'),
	'user_id': fields.many2one(obj='bc.users', label = 'User'),
	'active': fields.boolean(label = 'Active', store=True),
	# private partner
	'address_home_id': fields.many2one(obj='md.partner', label = 'Private Address', help='Enter here the private address of the employee, not the one linked to your company.'),
	'is_address_home_a_company': fields.boolean(label='The employee adress has a company linked',compute='_compute_is_address_home_a_company'),
	'country_id': fields.many2one(obj='md.country',label='Nationality (Country)'),
	'gender': fields.selection(selections=[
		('male', 'Male'),
		('female', 'Female'),
		('other', 'Other')
	],label="Gender"),
	'marital': fields.selection(selections=[
		('single', 'Single'),
		('married', 'Married'),
		('widower', 'Widower'),
		('divorced', 'Divorced')
	], label='Marital Status'),

	'ssnid': fields.varchar(label='SSN No', help='Social Security Number'),
	'sinid':fields.varchar(label='SIN No', help='Social Insurance Number'),
	'identification_id': fields.varchar(label='Identification No'),
	'passport_id': fields.varchar(label='Passport No'),
	#'bank_account_id': fields.many2one('res.partner.bank', 'Bank Account Number',domain="[('partner_id', '=', address_home_id)]",		help='Employee bank salary account'),
	'permit_no': fields.varchar(label='Work Permit No'),
	'visa_no': fields.varchar(label='Visa No'),
	'visa_expire': fields.date(label='Visa Expire Date'),

	# image: all image fields are base64 encoded and PIL-supported
	'image': fields.binary(label="Photo", accept='image/*', help="This field holds the image used as photo for the employee, limited to 1024x1024px."),
	'image_medium': fields.binary(label="Medium-sized photo", accept='image/*', help="Medium-sized photo of the employee. It is automatically "
			 "resized as a 128x128px image, with aspect ratio preserved. "
			 "Use this field in form views or some kanban views."),
	'image_small': fields.binary(label=	"Small-sized photo", accept='image/*', help="Small-sized photo of the employee. It is automatically "
			 "resized as a 64x64px image, with aspect ratio preserved. "
			 "Use this field anywhere a small image is required."),
	# work
	'address_id': fields.many2one(obj='md.partner', label='Work Address'),
	'work_phone':  fields.varchar(label='Work Phone'),
	'mobile_phone': fields.varchar(label='Work Mobile'),
	'work_email': fields.varchar(label='Work Email'),
	'work_location': fields.varchar('Work Location'),
	# employee in company
	'job_id': fields.many2one(obj='hcm.job', label='Job Position'),
	'department_id': fields.many2one(obj='hcm.department', label='Department'),
	'parent_id': fields.many2one(obj='hcm.employees', label='Manager'),
	'child_ids': fields.one2many(obj='hcm.employees', rel='parent_id', label='Subordinates',readonly=True),
	'coach_id': fields.many2one(obj='hcm.employees', label='Coach'),
	'category_ids': fields.many2many(obj='hcm.employee.categories', rel='hcm_employee_categories_rel', id2='category_id',id1='emp_id', label='Categories'),
	# misc
	'notes': fields.text('Notes'),
	'color': fields.integer('Color Index')
	}

	def _compute_is_address_home_a_company(self,record,context={}):
		return {'is_address_home_a_company':False}


	_default = {'active':True,'gender':'male','marital':'single','color':1}
	_groups = {'employee':['gender','marital','birthday','ssnid','sinid','identification_id','passport_id','bank_account_id']}

hcm_employees()

