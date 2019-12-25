inp = raw_input("Insert original string: ")
orig = inp
fin = raw_input("Insert the final string: ")
while True:
	try:
		lim = int(raw_input("Insert the rule usage limit: "))
		break
	except:
		pass

r1 = raw_input("Insert rule #1: ").replace(" ", "").split("=")
r2 = raw_input("Insert rule #2: ").replace(" ", "").split("=")
r3 = raw_input("Insert rule #3: ").replace(" ", "").split("=")
tooBig = False
found = False

# Sanity Checks
if r1[0] not in orig and r2[0] not in orig and r3[0] not in orig:
    print("Invalid rules")
    found = True
if len(inp) != len(fin):
    print("Invalid lengthed final")
    found = True
if lim < 0:
    print("Invalid length")
    found = True

#inp = "aabbcc"
#orig = inp
#fin = "cccccc"
#lim = 2
#r1 = ["aa", "bb"]
#r2 = ["bbb", "ccc"]
#r3 = ["b", "c"]

def loopFunc(curNest, curVal):
	global inp, found
	s = 0
	if curNest >= lim:
		#print curVal
		orig = inp
		
		for k in curVal:
			if k == 1:
				orig = orig.replace(r1[0], r1[1])
			if k == 2:
				orig = orig.replace(r2[0], r2[1])
			if k == 3:
				orig = orig.replace(r3[0], r3[1])
		if orig == fin:
			found = True
			c = 0
			print "0\t\t\t" + inp
			for k in curVal:
				if k == 1:
					c += 1
					inp = inp.replace(r1[0], r1[1])
					print str(c) + "\t" + r1[0] + " = " + r1[1] + "\t\t" + inp
				if k == 2:
					c += 1
					inp = inp.replace(r2[0], r2[1])
					print str(c) + "\t" + r2[0] + " = " + r2[1] + "\t\t" + inp
				if k == 3:
					c += 1
					inp = inp.replace(r3[0], r3[1])
					print str(c) + "\t" + r3[0] + " = " + r3[1] + "\t\t" + inp
			return True
		return False
	for a in range(0, 4):
		if loopFunc(curNest + 1, curVal + [a]):
			found = True
			return True

loopFunc(0, [])

if not found:
	print "Impossible"