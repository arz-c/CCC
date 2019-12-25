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

for i in range(10 ** lim):
	s = str(i).zfill(lim)
	val = []

	for j in s:
		#print j
		if int(j) >= 3:
			tooBig = True
			break
		val.append(int(j))
	#print s, val

	if(not tooBig):
		orig = inp
		tooBig = False

		for k in val:
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
			for k in val:
				c += 1
				if k == 1:
					inp = inp.replace(r1[0], r1[1])
					print str(c) + "\t" + r1[0] + " = " + r1[1] + "\t\t" + inp
				if k == 2:
					inp = inp.replace(r2[0], r2[1])
					print str(c) + "\t" + r2[0] + " = " + r2[1] + "\t\t" + inp
				if k == 3:
					inp = inp.replace(r3[0], r3[1])
					print str(c) + "\t" + r3[0] + " = " + r3[1] + "\t\t" + inp
			break

if not found:
	print "Impossible"