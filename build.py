import os
from functools import reduce
from os.path import join as opj
import sys
env=''
exclude = []
if len(sys.argv) > 1:
	exclude = sys.argv[2:]
	for d in os.walk(sys.argv[1]):
		l = list(map(lambda x:x[:-3],list(filter(lambda x: x[0] != '.' and x[-3:]=='.py' and  x not in exclude,d[2]))))
		if len(l) > 0:
			a=list(map(lambda x:opj(d[0],x), l ))
			env += ' ' + reduce(lambda x,y: x + ' ' + y, a)
	print(env[1:])
	
