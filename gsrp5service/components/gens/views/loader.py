import os
import json
from  os.path import join as opj
import web_pdb

_texts = {}
_gens = {}
_maps = {}

_frameworksdir = {'elementplus':'element-plus'}

def _loadFiles(path):
	folders = []
	for i in os.walk(path):
		folders.append(i)
		
	for address, dirs, files in folders:
		print(address, dirs, files)
		if address == path:
			continue
		for name in files:
			a1 = address.replace('./','').replace('/','-')
			af = a1.split('-')
			if af[0] in _frameworksdir:
				fw = _frameworksdir[af[0]]
			tv = af[1]
			bbb = name.split('.')
			nm,ext = bbb[0],bbb[1]
			if ext in ('template','script','style'):
				path = opj(address,name)
				if os.path.exists(path):
					if os.path.isfile(path) and not os.path.islink(path):
						with open(opj(address,name), 'r') as f:
							_texts[ext+ '-' + fw + '-' +'-'+tv+'-'+nm] = f.read()
					elif os.path.islink(path):
						link = os.readlink(path)
						a2 = link.split('.')[0]
						_maps[ext+ '-' + a1 + '-' +nm] = ext+ '-' + a1 + '-' + a2
			elif ext == 'py':
				_gens[a1] = __import__(name=address.replace('./','').replace('/','.') + '.' + nm,globals=globals(),locals=locals(),fromlist=[],level=0)

_loadFiles('./')

#for k in _texts.keys():
#	print('texts:',k,'\n',_texts[k])

#print('maps:',_maps)
print('texts:',_texts.keys())
print('gens:',_gens)

META = {'_texts':_texts,'_maps':_maps,'_gens':_gens}
