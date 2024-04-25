from functools import reduce

def concat(a,delimiter = '.'):
	if len(a) > 1:
		return reduce(lambda x,y: x + delimiter + y,a)
	elif len(a) == 1:
		return a[0]

def _remove_dirs(folders):
	import os, shutil
	if type(folders) == str:
		folders = [folders]
	for folder in folders:
		if os.path.exists(folder) and  os.path.isdir(folder):
			for filename in os.listdir(folder):
				file_path = os.path.join(folder, filename)
				try:
					if os.path.isfile(file_path) or os.path.islink(file_path):
						os.unlink(file_path)
					elif os.path.isdir(file_path):
						shutil.rmtree(file_path)
				except Exception as e:
					print('Failed to delete %s. Reason: %s' % (file_path, e))
	
