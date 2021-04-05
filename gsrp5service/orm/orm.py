import web_pdb

class Exception_Registry(Exception): pass

class ORM(object):
	@staticmethod
	def __inherits_cls__(registry,module, parser,meta):
		#web_pdb.set_trace()
		cls = _locals[parser]
		if module in registry._inherits and cls._obj in registry._inherits[module]:		
			for src in meta['attrs']['_inherits'].keys():
				last_module = registry._getLastModuleObjectLoaded(cls._obj,src)
				imeta = registry._objs[last_module][cls._obj][src]
				for key in meta['attrs']['_inherits'][src].keys():
					print('Mkey:',key,'__inherits_cls' + key + '__',hasattr(cls,'__inherits_cls' + key + '__'))
					if hasattr(cls,'__inherits_cls' + key + '__'):
						m = getattr(cls,'__inherits_cls' + key + '__', None)
						print('MM:','__inherits_cls' + key + '__',m)
						if m:
							if callable(m):
								m(meta,imeta,meta['attrs']['_inherits'][src][key])
							else:
								raise Exception('INHERIT: method: %s is`t callable' % (m,))
						else:
							raise Exception('INHERIT: method: %s not found' % ('___inherits_cls' + key + '__',))
	
				registry._objs[module][cls._obj][meta['attrs']['_name']] = meta

class INHERIT(object):
	@staticmethod
	def __inherit_cls__(registry,module, parser,imeta):
		#web_pdb.set_trace()
		cls = _locals[parser]
		if module in registry._inherit and cls._obj in registry._inherit[module]:		
			for dst in imeta['attrs']['_inherit'].keys():
				last_module = registry._getLastModuleObjectLoaded(cls._obj,dst)
				meta = registry._objs[last_module][cls._obj][dst]
				for key in imeta['attrs']['_inherit'][dst].keys():
					print('key:',key,'__inherit_cls' + key + '__',hasattr(cls,'__inherit_cls' + key + '__'))
					if hasattr(cls,'__inherit_cls' + key + '__'):
						m = getattr(cls,'__inherit_cls' + key + '__', None)
						print('M:','__inherit_cls' + key + '__',m)
						if m:
							if callable(m):
								m(meta,imeta,imeta['attrs']['_inherit'][dst][key])
							else:
								raise Exception('INHERIT: method: %s is`t callable' % (m,))
						else:
							raise Exception('INHERIT: method: %s not found' % ('___inherit_cls' + key + '__',))						
	
				registry._objs[module][cls._obj][dst] = meta
	
class Model(object):
	_obj = 'models'
	__keys_inherits__ = ['_columns','_actions','_states','_extra','_auths','_chechs','_views','trg_upd_cols','_trigers','_default','_constraints','_sql_constraints']				
	@staticmethod
	def __inherits_cls_methods__(meta, imeta, methods):
		for method in methods:
			if callable(imeta['attrs'][method]):
				meta['attrs'][method] = imeta['attrs'][method]

	@staticmethod
	def __inherits_cls_columns__(meta, imeta, columns):
		c = '_columns'
		for column in columns:
			if c not in meta['attrs'] or column not in meta['attrs'][c]:
				meta['attrs'].setdefault(c,{})[column] = imeta['attrs'][c][column]
			else:
				if imeta['attrs'][c][column]._type == 'iProperty':
					for attr in ('accept','actions','label', 'readonly','invisible', 'priority', 'domain', 'context', 'pattern','required', 'size', 'on_delete', 'on_update','on_change','on_check', 'translate', 'selections', 'selectable', 'manual', 'help', 'unique','check','family','timezone','relatedy','obj','rel','id1','id2','ref','offset','limit','compute','store','state','icon','cols','delimiter'):
						if attr in ('selections','domain','cols'):
							if hasattr(imeta['attrs'][c][column],attr):
								if hasattr(meta['attrs'][c][column],attr):
									getattr(meta['attrs'][c][column],attr).extend(getattr(imeta['attrs'][c][column],attr))
						elif attr in ('accept','label','priority','pattern','compute','readonly','on_change','on_check','invisible','on_delete','on_update','translate','selectable','manual','help','offset','limit','icon','delimiter'):
							if hasattr(imeta['attrs'][c][column],attr):
								if hasattr(meta['attrs'][c][column],attr):
									setattr(getattr(meta['attrs'][c][column],attr),attr,getattr(imeta['attrs'][c][column],attr))
						elif attr in ('actions','context','cols','state'):
							if hasattr(imeta['attrs'][c][column],attr):
								if hasattr(meta['attrs'][c][column],attr):
									getattr(meta['attrs'][c][column],attr).update(getattr(imeta['attrs'][c][column],attr))
				else:
					Exception_Registry("Column: %s of model: %s if exists\n" % (column,dst))
			
	@staticmethod
	def __inherits_cls_actions__(meta, imeta, actions):
		for action in actions:
			meta['attrs'].setdefault('_actions',{})[action] = imeta['attrs']['_actions'][action]

	@staticmethod
	def __inherits_cls_states__(meta, imeta, states):
		for state in states:
			meta['attrs'].setdefault('_states',{})[state] = imeta['attrs']['_states'][state]

	@staticmethod
	def __inherits_cls_defaults__(meta, imeta, dkeys):
		for dkey in dkeys:
			meta['attrs'].setdefault('_default',{})[dkey] = imeta['attrs']['_default'][dkey]

	@staticmethod
	def __inherits_cls_constraints(meta, imeta, constraints):
		meta['attrs'].setdefault('_constraints',[]).extend(imeta['attrs']['_constraints'])

	@staticmethod
	def __inherits_cls_sql_constraints__(meta, imeta, sql_constraints):
		meta['attrs'].setdefault('_sql_constraints',[]).extend(imeta['attrs']['_sql_constraints'])
	
	@staticmethod
	def __inherits_cls_auths__(meta, imeta, auths):
		meta['attrs'].setdefault('_auth',[]).extend(imeta['attrs']['_auth'])

	@staticmethod
	def __inherits_cls__(registry,module,meta):
		ORM.__inherits_cls__(registry,module,'Model',meta)

class Trigger(object): pass
class Report(object): pass
class Query(object): pass
class Dialog(object): pass
class Wizard(object): pass
class View(object): pass
class Dashboard(object): pass
class Link(object): pass


class ModelInherit(object):
	_obj = 'models'
	__keys_inherit__ = ['_columns','_actions','_states','_extra','_auths','_chechs','_views','trg_upd_cols','_trigers','_default','_constraints','_sql_constraints']				
	@staticmethod
	def __inherit_cls_methods__(meta, imeta, methods):
		for method in methods:
			if callable(imeta['attrs'][method]):
				meta['attrs'][action] = imeta['attrs'][method]

	@staticmethod
	def __inherit_cls_columns__(meta, imeta, columns):
		c = '_columns'
		for column in columns:
			if c not in meta['attrs'] or column not in meta['attrs'][c]:
				meta['attrs'].setdefault(c,{})[column] = imeta['attrs'][c][column]
			else:
				if imeta['attrs'][c][column]._type == 'iProperty':
					for attr in ('accept','actions','label', 'readonly','invisible', 'priority', 'domain', 'context', 'pattern','required', 'size', 'on_delete', 'on_update','on_change','on_check', 'translate', 'selections', 'selectable', 'manual', 'help', 'unique','check','family','timezone','relatedy','obj','rel','id1','id2','ref','offset','limit','compute','store','state','icon','cols','delimiter'):
						if attr in ('selections','domain','cols'):
							if hasattr(imeta['attrs'][c][column],attr):
								if hasattr(meta['attrs'][c][column],attr):
									getattr(meta['attrs'][c][column],attr).extend(getattr(imeta['attrs'][c][column],attr))
						elif attr in ('accept','label','priority','pattern','compute','readonly','on_change','on_check','invisible','on_delete','on_update','translate','selectable','manual','help','offset','limit','icon','delimiter'):
							if hasattr(imeta['attrs'][c][column],attr):
								if hasattr(meta['attrs'][c][column],attr):
									setattr(getattr(meta['attrs'][c][column],attr),attr,getattr(imeta['attrs'][c][column],attr))
						elif attr in ('actions','context','cols','state'):
							if hasattr(imeta['attrs'][c][column],attr):
								if hasattr(meta['attrs'][c][column],attr):
									getattr(meta['attrs'][c][column],attr).update(getattr(imeta['attrs'][c][column],attr))
				else:
					Exception_Registry("Column: %s of model: %s if exists\n" % (column,dst))
			
	@staticmethod
	def __inherit_cls_actions__(meta, imeta, actions):
		for action in actions:
			meta['attrs'].setdefault('_actions',{})[action] = imeta['attrs']['_actions'][action]

	@staticmethod
	def __inherit_cls_states__(meta, imeta, states):
		for state in states:
			meta['attrs'].setdefault('_states',{})[state] = imeta['attrs']['_states'][state]

	@staticmethod
	def __inherit_cls_defaults__(meta, imeta, dkeys):
		for dkey in dkeys:
			meta['attrs'].setdefault('_default',{})[dkey] = imeta['attrs']['_default'][dkey]

	@staticmethod
	def __inherit_cls_constraints(meta, imeta, constraints):
		meta['attrs'].setdefault('_constraints',[]).extend(imeta['attrs']['_constraints'])

	@staticmethod
	def __inherit_cls_sql_constraints__(meta, imeta, sql_constraints):
		meta['attrs'].setdefault('_sql_constraints',[]).extend(imeta['attrs']['_sql_constraints'])
	
	@staticmethod
	def __inherit_cls_auths__(meta, imeta, auths):
		meta['attrs'].setdefault('_auth',[]).extend(imeta['attrs']['_auth'])

	@staticmethod
	def __inherit_cls__(registry,module,imeta):
		INHERIT.__inherit_cls__(registry,module,'ModelInherit',imeta)
	
class TriggerInherit(object):
	def _trg_upd_cols(self, meta, imeta, trg_upd_cols):
		meta['attrs'].setdefault('_trg_upd_cols',[]).extend(imeta['attrs']['_trg_upd_cols'])

	def _trigers(self, meta, imeta, trigers):
		for triger in trigers:
			for tk in triger.keys():
				if not meta['attrs']['_trigers']:
					meta['attrs']['_trigers'] = []
				if type(triger[tk]) in ('list','tuple'):
					meta['attrs'].setdefault('_trigers',{}).setdefault(triger,[]).extend(triger[tk])
				else:
					meta['attrs'].setdefault('_trigers',{}).setdefault(triger,[]).append(triger[tk])

class ReportInherit(object): pass
class QueryInherit(object): pass
class DialogInherit(object): pass
class WizardInherit(object): pass
class ViewInherit(object): pass
class DashboardInherit(object): pass
class LinkInherit(object): pass

_locals = locals()

_maps = {'models':'Model','reports':'Report','triggers':'Triger','queries':'Query','dialogs':'Dialog','wizards':'Wizard','views':'View','dashboards':'Dashboard','links':'link'}

def inherit(registry,module,obj,imeta):
	return _locals[_maps[obj]+'Inherit'].__inherit_cls__(registry,module,imeta)

def inherits(registry,module,obj,meta):
	return _locals[_maps[obj]].__inherits_cls__(registry,module,meta)
