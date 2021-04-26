from lxml import etree
import json
from io import BytesIO
from gsrp5service.components.gens.views import isAllow
import web_pdb

def get_viewname_by_window_action_id(cr,pool,uid,action_id):
	action = pool.get('bc.actions').select(cr,pool,uid,fields=['view_id'],cond=[('name','=',action_id)])
	if len(action) > 0:
		oid = action[0]['view_id']['id']
		w = pool.get('bc.ui.views').read(cr,pool,uid,oid,fields=['name'])
		if len(w) > 0:
			return [w[0]['name']]
	
	return [None]

def get_viewname_by_window_action_id2(cr,pool,uid,action_id):
	views = pool.get('bc.view.actions').select(cr,pool,uid,fields=['view_id'],cond=[('action_id','=',action_id)])
	if len(views) > 0:
		oid = views[0]['view_id']['id']
		w = pool.get('bc.ui.views').read(cr,pool,uid,oid,fields=['name'])
		if len(w) > 0:
			return [w[0]['name']]
	
	return [None]


def get_model_by_window_action_id_v2(pool,action_id):
	ba = pool.get('bc.actions').select(fields=['name','ta',{'va':['view_id']},{'ra':['report_id']}],cond=[('name','=',action_id)])
	if len(ba) > 0:
		ta = ba[0]['ta']
		if ta == 'model':
			name = ba[0]['va'][0]['view_id']['name']
			action = pool.get('bc.ui.views').select(fields=['model'],cond=[('name','=',name)],limit=1)
			if len(action) > 0:
				return action[0]['model']
	return [None]

def get_view_by_window_action_id(cr,pool,uid,action_id):
	name = get_viewname_by_window_action_id(cr,pool,uid,action_id)
	if name[0]:
		return get_view_by_name(cr,pool,uid,name[0])
	return [None]

def get_view_by_name(cr,pool,uid,name):
	w = pool.get('bc.ui.views').select(cr,pool,uid,fields=['name','model','arch',{'inherit_views':['name','type','arch']}],cond=[('name','=',name)])[0]

	action = {}
	action['webicon'] = ''
	v = {'root':None,'models':{}}
	v['root'] = w['model']
	i = pool.get(w['model']).modelInfo() #[],{'columns':{'attributes':['type','compute','name','label','readonly','invisible','priority','required','unique','pattern','selections','selectable','size','domain','context','manual','help','default','timezone','ref','relatedy','obj','rel','id1','id2','offset','limit','accept','icon','cols','delimiter']}})
	v['models'][w['model']] = i

	for column in i['columns'].keys():
		if i['columns'][column]['type'] == 'referenced':
			ref = i['columns'][column]['ref'];
			field,reffield = ref.split('.')
			reffieldInfo = pool.get(i['columns'][field]['obj']).columnsInfo(columns=[reffield],attributes=['type','label','size'])
			if i['columns'][column]['label'] is None:
				i['columns'][column]['label'] = reffieldInfo[reffield]['label']
			i['columns'][column]['reftype'] = reffieldInfo[reffield]['type']
			if 'size' in reffieldInfo[reffield]:
				i['columns'][column]['size'] = reffieldInfo[reffield]['size']			

	for m in filter(lambda x:'obj' in i['columns'][x] and i['columns'][x]['obj'],i['columns'].keys()):
		obj = i['columns'][m]['obj']
		v['models'][obj] = pool.get(obj).modelInfo() #[],{'columns':('attributes':['type','compute','name','label','readonly','invisible','priority','required','unique','pattern','selections','selectable','size','domain','context','manual','help','default','timezone','ref','relatedy','obj','rel','id1','id2','offset','limit','accept','icon','cols','delimiter']}})

		m = v['models'][obj]
		for column in m['columns'].keys():
			if m['columns'][column]['type'] == 'referenced':
				ref = m['columns'][column]['ref'];
				field,reffield = ref.split('.')
				reffieldInfo = pool.get(m['columns'][field]['obj']).columnsInfo(columns=[reffield],attributes=['type','label','size'])
				if m['columns'][column]['label'] is None:
					m['columns'][column]['label'] = reffieldInfo[reffield]['label']
				m['columns'][column]['reftype'] = reffieldInfo[reffield]['type']
				if 'size' in reffieldInfo[reffield]:
					m['columns'][column]['size'] = reffieldInfo[reffield]['size']			
	
	mi = pool.get(w['model']).modelInfo()
	allow = list(filter(lambda x: isAllow(x,'models',mi),VIEWSGEN['models'].keys()))
	
	o = {'type':'','header':{},'columns':{},'viewname':w['name'],'webicon':action['webicon']}
	for event,el in etree.iterparse(source=BytesIO(w['arch'].encode('utf-8')),events=('end','start')):
		if el.tag in ('search','list','form','tree','kanban','graph','gantt','mdx','dashboard','calendar','schedule','geo','flow'):
			if event == 'start':
				o['type'] = el.tag
				for a in el.attrib:
					o['header'][a] = el.attrib[a]
			else:
				for inheritview in w['inherit_views']:
					for event,el in etree.iterparse(source=BytesIO(inheritview['arch'].encode('utf-8')),events=('end','start')):
						if el.tag in ('search','list','form','tree','kanban','graph','gantt','mdx','dashboard','calendar','schedule','geo','flow'):
							if event == 'end':
								pass
								#o['type'] = el.tag
								#for a in el.attrib:
									#o['header'][a] = el.attrib[a]
						
						elif el.tag == 'field':
							if event == 'end':
								name = el.attrib['name']
								o['columns'][name] = {}
								#print('FIELD:',name,columns[name]['type'])
								if name in i['columns']:
									for a in el.attrib:
										if a == 'name':
											continue
										o['columns'].setdefault(name,{})[a] = el.attrib[a]
		
		elif el.tag == 'field':
			if event == 'start':
				name = el.attrib['name']
				o['columns'][name] = {}
				#print('FIELD:',name,columns[name]['type'])
				if name in i['columns']:
					for a in el.attrib:
						if a == 'name':
							continue
						o['columns'].setdefault(name,{})[a] = el.attrib[a]
		
	v['view'] = o
	v['src'] = w['arch']
	v['allow'] = allow
	return [v,o,w['arch'],allow]
# v2
def get_views_of_model_v2(cr,pool,uid,model):
	v = {}
	v['root'] = 'view.' + model + '.search'
	info = pool.get(model).modelInfo() #[],{'columns':{'attributes':['type','compute','name','label','readonly','invisible','priority','required','unique','pattern','selections','selectable','size','domain','context','manual','help','default','timezone','ref','relatedy','obj','rel','id1','id2','offset','limit','accept','icon','cols','delimiter']}})

	v.setdefault('models',{}).setdefault(model,{})['meta'] = info

	m = v['models'][model]['meta']
	for column in m['columns'].keys():
		if m['columns'][column]['type'] == 'referenced':
			ref = m['columns'][column]['ref'];
			field,reffield = ref.split('.')
			reffieldInfo = pool.get(m['columns'][field]['obj']).columnsInfo(columns=[reffield],attributes=['type','label','size','selections'])
			print('reffieldInfo:',field,reffield,reffieldInfo)
			if m['columns'][column]['label'] is None:
				m['columns'][column]['label'] = reffieldInfo[reffield]['label']
			m['columns'][column]['reftype'] = reffieldInfo[reffield]['type']
			if 'size' in reffieldInfo[reffield]:
				m['columns'][column]['size'] = reffieldInfo[reffield]['size']			
			if 'selections' in reffieldInfo[reffield]:
				m['columns'][column]['selections'] = reffieldInfo[reffield]['selections']			


	views = pool.get('bc.ui.views').select(cr,pool,uid,fields=['name','model','arch',{'inherit_views':['name','type','arch']}],cond=[('model','=',model)])

	for view in views:
		o = parse_view_v2(view,info)
		v.setdefault('models',{}).setdefault(model,{}).setdefault('views',{})[o['type']] = o

	v['allow'] = list(filter(lambda x: isAllow(x,'models',info),VIEWSGEN['models'].keys()))	
	
	return [v]

def get_meta_of_model_v2(pool,model,context):
	trs = pool.get('bc.model.translations').select(['tr'],[('lang','=',context['lang']),('model','=',model)])
	m = pool.get(model)
	attrs = m.modelInfo() #attributes=['type','compute','name','label','readonly','invisible','priority','required','unique','pattern','selections','selectable','size','domain','context','manual','help','default','timezone','ref','relatedy','obj','rel','id1','id2','offset','limit','accept','icon','cols','delimiter'])
					
	#web_pdb.set_trace()
	if len(trs) > 0:
		tr = json.loads(trs[0]['tr'])
		attrs['description'] = tr['_description']
		for col in tr['_columns'].keys():
			for attr in tr['_columns'][col]:
				if col in attrs['columns'] and attr in attrs['columns'][col]:
					attrs['columns'][col][attr] = tr['_columns'][col][attr]
	
	return attrs
	
def get_meta_of_models_v2(pool,model,context):
	models = []
	m2mmodels = []
	m2omodels = []
	o2mmodels = []
	v = {}
	iobj = get_meta_of_model_v2(pool,model,context)

	for m in filter(lambda x:'obj' in iobj['columns'][x] and iobj['columns'][x]['obj'] and iobj['columns'][x]['type'] == 'one2many',iobj['columns'].keys()):
		models.append(iobj['columns'][m]['obj'])

	for m2o in filter(lambda x:'obj' in iobj['columns'][x] and iobj['columns'][x]['obj'] and iobj['columns'][x]['type'] in ('many2one','related'),iobj['columns'].keys()):
		m2omodels.append(iobj['columns'][m2o]['obj'])

	for m2m in filter(lambda x:'obj' in iobj['columns'][x] and iobj['columns'][x]['obj'] and iobj['columns'][x]['type'] == 'many2many',iobj['columns'].keys()):
		m2mmodels.append(iobj['columns'][m2m]['obj'])

	for o2m in filter(lambda x:'obj' in iobj['columns'][x] and iobj['columns'][x]['obj'] and iobj['columns'][x]['type'] == 'one2many',iobj['columns'].keys()):
		o2mmodels.append(iobj['columns'][o2m]['obj'])

	info = get_meta_of_model_v2(pool,model,context)
	views = get_views_of_model_v2(pool,model,info,context)
	info = get_referenced_attrs_v2(pool,info,context)
	
	v.setdefault(model,{})['meta'] = info
	v.setdefault(model,{})['views'] = views[model]  
	v.setdefault(model,{})['allow'] = list(filter(lambda x: isAllow(x,'models',info),VIEWSGEN['models'].keys()))

	for m2o in m2omodels:
		if m2o in v:
			continue
		m2oinfo = get_meta_of_model_v2(pool,m2o,context)
		m2oviews = get_views_of_model_v2(pool,m2o,m2oinfo,context)
		m2oinfo = get_referenced_attrs_v2(pool,m2oinfo,context)
		v.setdefault(m2o,{})['meta'] = m2oinfo
		v.setdefault(m2o,{})['views'] = m2oviews[m2o]  
		v.setdefault(m2o,{})['allow'] = list(filter(lambda x: isAllow(x,'models',m2oinfo),VIEWSGEN['models'].keys()))

	for m2m in m2mmodels:
		if m2m in v:
			continue
		m2minfo = get_meta_of_model_v2(pool,m2m,context)
		m2mviews = get_views_of_model_v2(pool,m2m,m2minfo,context)
		m2minfo = get_referenced_attrs_v2(pool,m2minfo,context)
		v.setdefault(m2m,{})['meta'] = m2minfo
		v.setdefault(m2m,{})['views'] = m2mviews[m2m]
		v.setdefault(m2m,{})['allow'] = list(filter(lambda x: isAllow(x,'models',m2minfo),VIEWSGEN['models'].keys())) 

	for m in models:
		if m == model or m in v:
			continue
		childs = get_meta_of_models_v2(pool,m,context)
		for k in childs.keys():
			if k not in v:
				v[k] = childs[k]

	#for o2m in filter(lambda x: x != model,o2mmodels):
		#v.setdefault(model,{}).setdefault('models', {})[o2m] = get_meta_of_models_v2(cr,pool,uid,o2m) 

	return v
			
def get_views_of_model_v2(pool,model,info,context):
	o = {}

	views = pool.get('devel.ui.model.views').select(fields=['fullname','framework','model','vtype','standart','template','script','style','scoped','sfc',{'cols':['col']},{'inherit_cols':['col']}],cond=[('framework','=',context['framework']),('model','=',model)],context=context)
	for view in views:
		confs = pool.get('devel.tuning.ui.model.views').select(fields=['fullname','name','view','tuser','values'],cond=[('view','=',view['name']),('tuser','=', context['user'])],context=context)
		v  = {'columns':[],'id':view['id'],'confs':confs}
		v['columns'].extend(view['cols'])
		v['columns'].extend(view['inherit_cols'])
		
		o[view['vtype']] = v

	return {model:o}

def get_views_of_model_v2_2(pool,model,info,context):
	o = {}
	views = pool.get('bc.ui.views').select(fields=['name','model','arch',{'inherit_views':['name','type','arch']}],cond=[('model','=',model)],context=context)
	for view in views:
		confs = pool.get('bc.tuning.ui.views').select(fields=['name','tuser','values'],cond=[('view','=',view['name']),('tuser','r=',pool.get('bc.tuning.ui.views')._uid)],context=context)
		v = parse_view_v2(view,info,context)
		v['id'] = view['id']
		v['confs'] = confs
		o[v['type']] = v

	return {model:o}
	

	
def get_view_by_window_action_id_v2(cr,pool,uid,action_id):
	name = get_viewname_by_window_action_id2(cr,pool,uid,action_id)
	if name[0]:
		return get_view_by_name_v2(cr,pool,uid,name[0])
	return [None]

def get_meta_by_window_action_id_v2(pool,action_id,context):
	#web_pdb.set_trace()
	model = get_model_by_window_action_id_v2(pool,action_id)
	mof = get_meta_of_models_v2(pool,model,context)
	return [{'root':model,'models':mof}]

def get_view_by_name_v2(cr,pool,uid,name):
	action = {}
	action['webicon'] = ''

	v = {'root':None,'models':{},}
	
	w = pool.get('bc.ui.views').select(cr,pool,uid,fields=['name','model','arch',{'inherit_views':['name','type','arch']}],cond=[('name','=',name)])[0]
	
	v['root'] = w['model']
	
	models = [v['root']]

	iobj = pool.get(w['model']).modelInfo() #attributes=['type','compute','name','label','readonly','invisible','priority','required','unique','pattern','selections','selectable','size','domain','context','manual','help','default','timezone','ref','relatedy','obj','rel','id1','id2','offset','limit','accept','icon','cols','delimiter'])

	
	for m in filter(lambda x:'obj' in iobj['columns'][x] and iobj['columns'][x]['obj'],iobj['columns'].keys()):
		models.append(iobj['columns'][m]['obj'])

	for model in models:
		info = pool.get(model).modelInfo() #attributes=['type','compute','name','label','readonly','invisible','priority','required','unique','pattern','selections','selectable','size','domain','context','manual','help','default','timezone','ref','relatedy','obj','rel','id1','id2','offset','limit','accept','icon','cols','delimiter'])

		v['models'].setdefault(model,{})['meta'] = info

		m = v['models'][model]['meta']
		for column in m['columns'].keys():
			if m['columns'][column]['type'] == 'referenced':
				ref = m['columns'][column]['ref'];
				field,reffield = ref.split('.')
				reffieldInfo = pool.get(m['columns'][field]['obj']).columnsInfo(columns=[reffield],attributes=['type','label','size','selections'])
				if m['columns'][column]['label'] is None:
					m['columns'][column]['label'] = reffieldInfo[reffield]['label']
				m['columns'][column]['reftype'] = reffieldInfo[reffield]['type']
				if 'size' in reffieldInfo[reffield]:
					m['columns'][column]['size'] = reffieldInfo[reffield]['size']						
				if 'selections' in reffieldInfo[reffield]:
					m['columns'][column]['selections'] = reffieldInfo[reffield]['selections']						
		views = pool.get('bc.ui.views').select(cr,pool,uid,fields=['name','model','arch',{'inherit_views':['name','type','arch']}],cond=[('model','=',model)])

		for view in views:
			o = parse_view_v2(view,info)
			v.setdefault('models',{}).setdefault(model,{}).setdefault('views',{})[o['type']] = o

	v['allow'] = list(filter(lambda x: isAllow(x,'models',iobj),VIEWSGEN['models'].keys()))	
	
	return [v]

def parse_view_v2(w,info,context):
	
	o = {'type':'','header':{},'columns':{},'viewname':w['name'],'webicon':''}
	for event,el in etree.iterparse(source=BytesIO(w['arch'].encode('utf-8')),events=('end','start')):
		if el.tag in ('search','find','list','m2mlist','form','tree','kanban','graph','gantt','mdx','dashboard','calendar','schedule','geo','flow'):
			if event == 'start':
				o['type'] = el.tag
				for a in el.attrib:
					o['header'][a] = el.attrib[a]
			else:
				for inheritview in w['inherit_views']:
					for event,el in etree.iterparse(source=BytesIO(inheritview['arch'].encode('utf-8')),events=('end','start')):
						if el.tag in ('search','find','list','m2mlist','form','tree','kanban','graph','gantt','mdx','dashboard','calendar','schedule','geo','flow'):
							if event == 'end':
								pass
								#o['type'] = el.tag
								#for a in el.attrib:
									#o['header'][a] = el.attrib[a]
						
						elif el.tag == 'field':
							if event == 'end':
								name = el.attrib['name']
								o['columns'][name] = {}
								#print('FIELD:',name,columns[name]['type'])
								if name in info['columns']:
									for a in el.attrib:
										if a == 'name':
											continue
										o['columns'].setdefault(name,{})[a] = el.attrib[a]
		
		elif el.tag == 'field':
			if event == 'start':
				name = el.attrib['name']
				o['columns'][name] = {}
				#print('FIELD:',name,columns[name]['type'])
				if name in info['columns']:
					for a in el.attrib:
						if a == 'name':
							continue
						o['columns'].setdefault(name,{})[a] = el.attrib[a]
		
	return o


	
# old
def view(cr,pool,uid,action_id = None, name = None):
	if action_id:
		action = pool.get('bc.actions').select(cr,pool,uid,fields=['name','view_id','webicon'],cond=[('name','=',action_id)])[0]
		oid = action['view_id']['id']
		
		w = pool.get('bc.ui.views').read(cr,pool,uid,oid,fields=['name','model','arch'])[0]
		
	if name:
		w = pool.get('bc.ui.views').select(cr,pool,uid,fields=['name','model','arch'],cond=[('name','=',name)])[0]

		action = {}
		action['webicon'] = ''
	v = {'root':None,'models':{}}
	v['root'] = w['model']
	i = pool.get(w['model']).modelInfo() #attributes=['type','compute','name','label','readonly','invisible','priority','required','unique','pattern','selections','selectable','size','domain','context','manual','help','default','timezone','relatedy','obj','rel','id1','id2','offset','limit','ref','accept','icon','cols','delimiter'])
	v['models'][w['model']] = i

	for column in i['columns'].keys():
		if i['columns'][column]['type'] == 'referenced':
			ref = i['columns'][column]['ref'];
			field,reffield = ref.split('.')
			reffieldInfo = pool.get(i['columns'][field]['obj']).columnsInfo(columns=[reffield],attributes=['type','label','size'])
			if i['columns'][column]['label'] is None:
				i['columns'][column]['label'] = reffieldInfo[reffield]['label']
			i['columns'][column]['reftype'] = reffieldInfo[reffield]['type']
			if 'size' in reffieldInfo[reffield]:
				i['columns'][column]['size'] = reffieldInfo[reffield]['size']			

	for m in filter(lambda x:'obj' in i['columns'][x] and i['columns'][x]['obj'],i['columns'].keys()):
		obj = i['columns'][m]['obj']
		v['models'][obj] = pool.get(obj).modelInfo() #attributes=['type','compute','name','label','readonly','invisible','priority','required','unique','pattern','selections','selectable','size','domain','context','manual','help','default','timezone','relatedy','obj','rel','id1','id2','offset','limit','ref','icon','cols','delimiter'])

		m = v['models'][obj]
		for column in m['columns'].keys():
			if m['columns'][column]['type'] == 'referenced':
				ref = m['columns'][column]['ref'];
				field,reffield = ref.split('.')
				reffieldInfo = pool.get(m['columns'][field]['obj']).columnsInfo(columns=[reffield],attributes=['type','label','size'])
				if m['columns'][column]['label'] is None:
					m['columns'][column]['label'] = reffieldInfo[reffield]['label']
				m['columns'][column]['reftype'] = reffieldInfo[reffield]['type']
				if 'size' in reffieldInfo[reffield]:
					m['columns'][column]['size'] = reffieldInfo[reffield]['size']			
	
	mi = pool.get(w['model']).modelInfo()
	allow = list(filter(lambda x: isAllow(x,'models',mi),VIEWSGEN['models'].keys()))
	
	o = {'type':'','header':{},'columns':{},'viewname':w['name'],'webicon':action['webicon']}
	for event,el in etree.iterparse(source=BytesIO(w['arch'].encode('utf-8')),events=('end','start')):
		if el.tag in ('search','list','form'):
			if event == 'start':
				o['type'] = el.tag
				for a in el.attrib:
					o['header'][a] = el.attrib[a]
		
		elif el.tag == 'field':
			if event == 'start':
				name = el.attrib['name']
				o['columns'][name] = {}
				#print('FIELD:',name,columns[name]['type'])
				if name in i['columns']:
					for a in el.attrib:
						if a == 'name':
							continue
						o['columns'].setdefault(name,{})[a] = el.attrib[a]
	
	return [v,o,w['arch'],allow]

def get_referenced_attrs_v2(pool,info,context):
	for column in info['columns'].keys():
		if info['columns'][column]['type'] == 'referenced':
			ref = info['columns'][column]['ref'];
			field,reffield = ref.split('.')
			reffieldInfo = pool.get(info['columns'][field]['obj']).columnsInfo(columns=[reffield],attributes=['type','label','size','selections'])
			if info['columns'][column]['label'] is None:
				info['columns'][column]['label'] = reffieldInfo[reffield]['label']
			info['columns'][column]['reftype'] = reffieldInfo[reffield]['type']
			if 'size' in reffieldInfo[reffield]:
				info['columns'][column]['size'] = reffieldInfo[reffield]['size']						
			if 'selections' in reffieldInfo[reffield]:
				info['columns'][column]['selections'] = reffieldInfo[reffield]['selections']					

	return info
