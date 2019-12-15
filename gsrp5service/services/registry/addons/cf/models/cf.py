from gsrp5service.orm import fields
from gsrp5service.orm.model import Model,ModelInherit

from datetime import datetime

from passlib.hash import pbkdf2_sha256

class cf_groups(Model):
	_name = 'cf.groups'
	_description = 'General Model Colobrative Groups'
	_columns = {
	'name': fields.varchar(label = 'Name',size=128),
	'code': fields.integer(label='Code'),
	'users_id': fields.many2many(label='Grpup',obj='bc.users',rel='cf_user_group_rel',id2='users_id',id1='groups_id')
	}

cf_groups()

class cf_tags(Model):
	_name = 'cf.tags'
	_description = 'General Model Colobrative Folders File Tags'
	_rec_name = 'tag'
	_columns = {
	'tag': fields.varchar(label = 'Tag',size=64),
	'folders': fields.many2many(label='Folders',obj='cf.folders',rel='cf_folder_tags_rel',id2='folder_id',id1='tag_id'),
	'files': fields.many2many(label='Files',obj='cf.files',rel='cf_file_tags_rel',id2='file_id',id1='tag_id'),
	'links': fields.many2many(label='Links',obj='cf.links',rel='cf_link_tags_rel',id2='link_id',id1='tag_id')
	}

cf_tags()

class cf_file_access_users(Model):
	_name = 'cf.file.access.users'
	_description = 'General Model File Access Users'
	_columns = {
	'file_id': fields.many2one(label='File',obj='cf.files'),
	'user_id': fields.many2one(label='User',obj='bc.users'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':True,
	'x':True
	}

cf_file_access_users()

class cf_file_access_groups(Model):
	_name = 'cf.file.access.groups'
	_description = 'General Model File Access Groups'
	_columns = {
	'file_id': fields.many2one(label='File',obj='cf.files'),
	'group_id': fields.many2one(label='Group',obj='cf.groups'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':False,
	'x':True
	}

cf_file_access_groups()

class cf_file_access_others(Model):
	_name = 'cf.file.access.others'
	_description = 'General Model File Access Others'
	_columns = {
	'file_id': fields.many2one(label='File',obj='cf.files'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':False,
	'x':False
	}

cf_file_access_others()

class cf_files(Model):
	_name = 'cf.files'
	_description = 'General Model Colobrative Files'
	_log_access = False
	_columns = {
	'name': fields.varchar(label = 'Name',size=64),
	'size': fields.integer(label='Size',readonly=True),
	'created_by': fields.many2one(label='Created By',obj='bc.users',readonly=True),
	'created': fields.datetime(label='Created',readonly=True),
	'modified_by': fields.many2one(label='Modified By',obj='bc.users',readonly=True),
	'modified': fields.datetime(label='Modified',readonly=True),
	'url': fields.varchar(label='Url'),
	'data':fields.binary(label='Data',accept='*'),
	'folder_id': fields.many2one(label='Folder',obj='cf.folders'),
	'users_access': fields.one2many(label='User Access',obj='cf.file.access.users',rel='file_id'),
	'groups_access': fields.one2many(label='Group Access',obj='cf.file.access.groups',rel='file_id'),
	'others_access': fields.one2many(label='Other Access',obj='cf.file.access.others',rel='file_id'),
	'tags_id': fields.many2many(label='Tags',obj='cf.tags',rel='cf_files_tags_rel',id1='file_id',id2='tag_id')
	}
	
	def create(self, cr, pool, uid, records,context = {}):
		if type(records) == dict:
			records['created_by'] = uid
			records['created'] = datetime.utcnow().astimezone()
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['created_by'] = uid
				record['created'] = dt

		return super(Model,self).create(cr, pool, uid, records, context)

	def write(self, cr, pool, uid, records, context = {}):
		if type(records) == dict:
			records['modified_by'] = uid
			records['modified'] = datetime.utcnow().astimezone()
			
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['modified_by'] = uid
				record['modified'] = dt

		return super(Model,self).write(cr, pool, uid, records, context)

	def modify(self, cr, pool, uid, records,context = {}):
		if type(records) == dict:
			records['modified_by'] = uid
			records['modified'] = datetime.utcnow().astimezone()
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['modified_by'] = uid
				record['modified'] = dt

		return super(Model,self).modify(cr, pool, uid, records, context)

cf_files()

# Links
class cf_link_access_users(Model):
	_name = 'cf.link.access.users'
	_description = 'General Model Link Access Users'
	_columns = {
	'link_id': fields.many2one(label='Link',obj='cf.links'),
	'user_id': fields.many2one(label='User',obj='bc.users'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':True,
	'x':True
	}

cf_link_access_users()

class cf_link_access_groups(Model):
	_name = 'cf.link.access.groups'
	_description = 'General Model Link Access Groups'
	_columns = {
	'link_id': fields.many2one(label='Link',obj='cf.links'),
	'group_id': fields.many2one(label='Group',obj='cf.groups'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':False,
	'x':True
	}

cf_link_access_groups()

class cf_link_access_others(Model):
	_name = 'cf.link.access.others'
	_description = 'General Model Link Access Others'
	_columns = {
	'link_id': fields.many2one(label='Link',obj='cf.links'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':False,
	'x':False
	}

cf_link_access_others()

class cf_links(Model):
	_name = 'cf.links'
	_description = 'General Model Colobrative Links'
	_log_access = False
	_columns = {
	'name': fields.varchar(label = 'Name',size=64),
	'file_id': fields.many2one(label='File',obj='cf.files'),
	'created_by': fields.many2one(label='Created By',obj='bc.users'),
	'created': fields.datetime(label='Created'),
	'modified_by': fields.many2one(label='Modified By',obj='bc.users'),
	'modified': fields.datetime(label='Modified'),
	'folder_id': fields.many2one(label='Folder',obj='cf.folders'),
	'users_access': fields.one2many(label='User Access',obj='cf.link.access.users',rel='link_id'),
	'groups_access': fields.one2many(label='Group Access',obj='cf.link.access.groups',rel='link_id'),
	'others_access': fields.one2many(label='Other Access',obj='cf.link.access.others',rel='link_id'),
	'tags_id': fields.many2many(label='Tags',obj='cf.tags',rel='cf_links_tags_rel',id1='link_id',id2='tag_id')

	}

	def create(self, cr, pool, uid, records,context = {}):
		if type(records) == dict:
			records['created_by'] = uid
			records['created'] = datetime.utcnow().astimezone()
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['created_by'] = uid
				record['created'] = dt

		return super(Model,self).create(cr, pool, uid, records, context)

	def write(self, cr, pool, uid, records, context = {}):
		if type(records) == dict:
			records['modified_by'] = uid
			records['modified'] = datetime.utcnow().astimezone()
			
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['modified_by'] = uid
				record['modified'] = dt

		return super(Model,self).write(cr, pool, uid, records, context)

	def modify(self, cr, pool, uid, records,context = {}):
		if type(records) == dict:
			records['modified_by'] = uid
			records['modified'] = datetime.utcnow().astimezone()
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['modified_by'] = uid
				record['modified'] = dt

		return super(Model,self).modify(cr, pool, uid, records, context)

cf_links()

# Folders
class cf_folder_access_users(Model):
	_name = 'cf.folder.access.users'
	_description = 'General Model File Access Users'
	_columns = {
	'folder_id': fields.many2one(label='User',obj='cf.folders'),
	'user_id': fields.many2one(label='User',obj='bc.users'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':True,
	'x':True
	}

cf_folder_access_users()

class cf_folder_access_groups(Model):
	_name = 'cf.folder.access.groups'
	_description = 'General Model Folder Access Groups'
	_columns = {
	'folder_id': fields.many2one(label='User',obj='cf.folders'),
	'group_id': fields.many2one(label='Group',obj='cf.groups'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':False,
	'x':True
	}

cf_folder_access_groups()

class cf_folder_access_others(Model):
	_name = 'cf.folder.access.others'
	_description = 'General Model Folder Access Others'
	_columns = {
	'folder_id': fields.many2one(label='Folder',obj='cf.folders'),
	'r': fields.boolean(label = 'Read'),
	'w': fields.boolean(label = 'Write'),
	'x': fields.boolean(label = 'Exec'),
	}
	
	_default = {
	'r':True,
	'w':False,
	'x':False
	}

cf_folder_access_others()

class cf_folders(Model):
	_name = 'cf.folders'
	_description = 'General Model Colobrative Folders'
	_log_access = False
	_columns = {
	'name': fields.varchar(label = 'Name',size=64),
	'created_by': fields.many2one(label='Created By',obj='bc.users'),
	'created': fields.datetime(label='Created'),
	'modified_by': fields.many2one(label='Modified By',obj='bc.users'),
	'modified': fields.datetime(label='Modified'),
	'parent_id': fields.many2one(label='Parent',obj='cf.folders'),
	'childs_id': fields.one2many(label='Childs',obj='cf.folders',rel='parent_id'),
	'files': fields.one2many(label='Files',obj='cf.files',rel='folder_id'),
	'links': fields.one2many(label='Links',obj='cf.links',rel='link_id'),
	'users_access': fields.one2many(label='User Access',obj='cf.folder.access.users',rel='folder_id'),
	'groups_access': fields.one2many(label='Group Access',obj='cf.folder.access.groups',rel='folder_id'),
	'others_access': fields.one2many(label='Other Access',obj='cf.folder.access.others',rel='folder_id'),
	'tags_id': fields.many2many(label='Tags',obj='cf.tags',rel='cf_folder_tags_rel',id1='folder_id',id2='tag_id')
	}

	def create(self, cr, pool, uid, records,context = {}):
		if type(records) == dict:
			records['created_by'] = uid
			records['created'] = datetime.utcnow().astimezone()
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['created_by'] = uid
				record['created'] = dt

		return super(Model,self).create(cr, pool, uid, records, context)

	def write(self, cr, pool, uid, records, context = {}):
		if type(records) == dict:
			records['modified_by'] = uid
			records['modified'] = datetime.utcnow().astimezone()
			
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['modified_by'] = uid
				record['modified'] = dt
		
		return super(Model,self).write(cr, pool, uid, records, context)

	def modify(self, cr, pool, uid, records,context = {}):
		if type(records) == dict:
			records['modified_by'] = uid
			records['modified'] = datetime.utcnow().astimezone()
		elif type(records) in (list,tuple):
			dt = datetime.utcnow().astimezone()
			for record in records:
				record['modified_by'] = uid
				record['modified'] = dt

		return super(Model,self).modify(cr, pool, uid, records, context)

cf_folders()
