from functools import reduce
from lxml import etree
from io import BytesIO

_VIEWTAGS = ('form','list','table','tree','calendar','graph','gantt','mdx')
_ELTAGS = ('field','page','delimiter')
_TAGS = _VIEWTAGS+_ELTAGS

relaxng = etree.RelaxNG(file='views.rng')

class FormView(object):

	def __init__(self, el):
		self.attrs = dict(el.items())
		self.text = el.text
		self.child = []
		self.iw= etree.iterwalk(el,events=('start',), tag = ('field','page','delimiter'))

	def parse(self):
		
		for ev,el in self.iw:
			if ev == 'start':
				p = el.getparent()
				if not p or p and p.tag == 'form':
					self.child.append(_TAGPARSERS[el.tag](el))

	def result(self):
		return ['form',self.attrs,self.text,self.child]

def ValidateXML(view):
	isXMLValid = False
	try:
		doc = etree.parse(view)
		isXMLValid = relaxng.assert_(doc)
		if isXMLValid is None:
			isXMLValid = True
	except:
		log = relaxng.error_log
		print(log.last_error)
	return isXMLValid


def ViewParsePage(page):
	childs = []
	iw= etree.iterwalk(page,events=('start','end','start-ns','end-ns'), tag = ('field','delimiter'))
	for event,element in iw:
		if event == 'start':
			p = element.getparent()
			if p is not None or p and p.tag == page.tag:	
				childs.append(_TAGPARSERS[element.tag](element))
	return ['page', dict(page.items()),page.text,childs]

def ViewParseField(field):
	return ['field',dict(field.items()),field.text]

def ViewParseDelimiter(el):
	return ['delimiter']


def ViewParseViews(view):
	childs = []
	iw= etree.iterwalk(view,events=('start','end','start-ns','end-ns'), tag = _ELTAGS)
	for event,element in iw:
		if event == 'start':
			p = element.getparent()
			if p is not None and p.tag == view.tag:
				childs.append(_TAGPARSERS[element.tag](element))
				
	return [view.tag,dict(view.items()),view.text,childs]


_TAGPARSERS = {'form':ViewParseViews, 'list':ViewParseViews,'table':ViewParseViews,'tree':ViewParseViews,'calendar':ViewParseViews,'graph':ViewParseViews,'gantt':ViewParseViews,'mdx':ViewParseViews,'field':ViewParseField,'page':ViewParsePage,'delimiter':ViewParseDelimiter}

def ViewParse(view):
	f = BytesIO(bytes(view,'utf8'))
	if not ValidateXML(f):
		return []
	else:
		print('Validate')
	result = []
	i = etree.iterparse(f,events = ('start','end','start-ns','end-ns'),tag = _VIEWTAGS)
	for event,element in i:
		if event == 'start':
			if element.tag in _VIEWTAGS:
				result = _TAGPARSERS[element.tag](element)
		elif event == 'end':
			pass
		elif event == 'start-ns':
			pass
		elif event == 'end-ns':
			pass
	
	return result

def GetFieldsViews(view):
	res = []
	for el in view:
		if el[0] == 'field':
			res.append(GetFieldsField(el))
		elif el[0] == 'delimiter':
			pass
		elif el[0] == 'page':
			res.extend(_FIELDGETTERS[el[0]](el[3]))
	return res

def GetFieldsPage(page):
	res = []
	for el in page:
		if el[0] == 'field':
			res.append(GetFieldsField(el))
		elif el[0] == 'delimiter':
			pass
		elif el[0] == 'page':
			res.extend(_FIELDGETTERS[el[0]](el[3]))
	return res

def GetFieldsField(field):
	return field[1]['name']

	
_FIELDGETTERS = {'form':GetFieldsViews,'list':GetFieldsViews, 'table':GetFieldsViews,'tree':GetFieldsViews,'graph':GetFieldsViews,'calendar':GetFieldsViews,'gantt':GetFieldsViews,'mdx':GetFieldsViews,'field':GetFieldsField,'page':GetFieldsPage}

def GetFields(model):
	if len(model) > 2 and model[0] in _FIELDGETTERS:
		return _FIELDGETTERS[model[0]](model[3])
	else:
		return []

if __name__ == "__main__":
	xmlform="""<?xml version="1.0"?>
	<form model="bc.users" name="bc.users.form" sortable="1" parent="parent_id" childs="childs_id">Text A
	  <field name="login">Text B</field>
	  <field name="password">Text C	</field>
	  
      <page name="active">Page 1
		<field name="created">Created</field>
		<field name="created_by">Created By</field>
	  </page>
	  <delimiter/>
	</form>"""

	xmltree="""<?xml version="1.0"?>
	<tree model="bc.users" name="bc.users.form" sortable="1" parent="parent_id" childs="childs_id">Text A
	  <field name="login">Text B</field>
	  <field name="password">Text C	</field>
      <field name="created">Created</field>
	  <field name="created_by">Created By</field>
	</tree>"""
	
	xmllist="""<?xml version="1.0"?>
	<list model="bc.users" name="bc.users.form">Text A
	  <field name="login">Text B</field>
	  <field name="password">Text C	</field>
      <field name="created">Created</field>
	  <field name="created_by">Created By</field>
	</list>"""

	xmlgraph="""<?xml version="1.0"?>
	<graph model="bc.users" name="bc.users.form" chart="pie">Text A
	  <field name="login">Text B</field>
	  <field name="password">Text C	</field>
      <field name="created">Created</field>
	  <field name="created_by">Created By</field>
	  <field name="Value">Value</field>
	</graph>"""


	views = [xmlform,xmltree,xmllist,xmlgraph]
	for view in views:	
		meta = ViewParse(view)
		fields = GetFields(meta)
		print('meta:',meta)
		print('meta:',fields)
