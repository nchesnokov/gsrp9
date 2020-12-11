from functools import reduce

def concat(a,delimiter = '.'):
	if len(a) > 1:
		return reduce(lambda x,y: x + delimiter + y,a)
	elif len(a) == 1:
		return a[0]
