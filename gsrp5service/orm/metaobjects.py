from functools import reduce
import web_pdb

_objects = ['dashboard','model','report','view','query','dialog','wizard','link','metaobjects']

class MetaObjects(type):
	__objects__ = {}

	def __new__(cls, name, bases, attrs):
		if '__module__' in attrs:
			_m = attrs['__module__'].split('.')
			if len(_m) >  2 and _m[2] not in _objects: 
				_m = attrs['__module__'].split('.')
				_module = attrs['__module__']
	
				if _m[0] == 'gsrp5service':
					_module = reduce(lambda x,y: x + '.' + y,attrs['__module__'].split('.')[4:5])
					_obj = 	attrs['__module__'].split('.')[5]	
				else:	
					_module = reduce(lambda x,y: x + '.' + y,attrs['__module__'].split('.')[1:2])
					_obj = 	attrs['__module__'].split('.')[2]
					
				MetaObjects.__objects__.setdefault(_module,{}).setdefault(_obj,{})[attrs['_name']] = {'name':name,'bases':bases,'attrs':attrs}

		return super(MetaObjects, cls).__new__(cls, name, bases, attrs)

	def __init__(self, name, bases, attrs):
		if not hasattr(self, '_register'):
			setattr(self,'_register',True)
		else:
			self._register = True
			super(MetaObjects, self).__init__(name, bases, attrs)
