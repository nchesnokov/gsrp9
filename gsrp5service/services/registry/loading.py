import os
import sys
import importlib
from os.path import join as opj

def load_resource_from_file(path,name,mode = "rb"):
	if  os.path.exists(opj(path, name)) and os.path.isfile(opj(path, name)):
		try:
			with open(opj(path, name), mode) as f:
				d = f.read()
				f.close()
				return d
		finally:
			try:
				f.close()
			except:
				pass

	else:
		return None

def load_module(name,fromlist = ()):
	return __import__(name=name,globals=globals(),locals=locals(),fromlist=fromlist)

def load_module_info(path):
	i = load_resource_from_file(path,'__manifest__.info','rb')
	if i:
		return eval(i)
	else:
		return {}
