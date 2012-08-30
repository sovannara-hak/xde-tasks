def isIn(sublist, reflist):
	if not sublist:
		return True
	try:
		elementIndex = reflist.index(sublist[0])
		return isIn(sublist[1:], reflist[0:elementIndex]+reflist[elementIndex+1:])
	except:
		return False
