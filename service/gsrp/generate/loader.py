import os
import json
from  os.path import join as opj
import web_pdb

_texts = {}
_gens = {}
_maps = {}

_frameworksdir = {'elementplus':'element-plus'}

def _loadFiles(path):
	fw = ''
	for d in filter(lambda x: os.path.isdir(opj(path,x)),os.listdir(path)):
		if os.path.isdir(opj(path,d)) and d in _frameworksdir:
			fw = _frameworksdir[d]
		else:
			continue
		for address, dirs, files in os.walk(opj(path,d)):
			if address[-11:] == '__pycache__':
				continue
			v = address.partition(path + os.path.sep)[2].replace('./','').split(os.path.sep)
			if len(v) > 1:
				_gens[fw+'/'+v[1]] = __import__(name='gsrp5service.generate.'+ d +'.' +v[1] ,globals=globals(),locals=locals(),fromlist=['view'],level=0)
			for name in files:
				if address.startswith('./'):
					k1 = address.replace('./','').split(os.path.sep)
					if len(k1) <= 1:
						continue
					k = '-'.join(k1[1:])					
				else:
					k = '-'.join(address.partition(path+os.path.sep)[2].split(os.path.sep)[1:])
				nm,ext = name.split('.')
				if ext in ('template','script','style'):
					p = opj(address,name)
					if os.path.exists(p):
						if os.path.isfile(p) and not os.path.islink(p):
							with open(opj(p), 'r') as f:
								_texts[ext+ '-' + fw + '-' + k + '-' + nm] = f.read()
						elif os.path.islink(p):
							link = os.readlink(p)
							a2 = link.partition(path+os.path.sep)[0].split('.')[0]
							_maps[ext+ '-' + fw + '-'  + k + '-' + nm] = ext+ '-' + fw + '-' + k + '-' + a2

if __name__ == '__main__':
	_loadFiles('./')
	print('MAPS:',_maps)
	print('TEXTS:',_texts.keys())
	print('GENS:',_gens)
	
	for k in _gens.keys():
		print('GENS:',k,dir(_gens[k]))
else:
	_loadFiles(os.path.dirname(__file__))

META = {'_texts':_texts,'_maps':_maps,'_gens':_gens}
