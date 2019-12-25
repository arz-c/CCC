inp = raw_input("Insert original string: ")
orig = inp
fin = raw_input("Insert the final string: ")
lim = int(raw_input("Insert the rule usage limit: "))
r1 = raw_input("Insert rule #1: ").replace(" ", "").split("=")
r2 = raw_input("Insert rule #2: ").replace(" ", "").split("=")
r3 = raw_input("Insert rule #3: ").replace(" ", "").split("=")
done = False

# Sanity Checks
if r1[0] not in orig and r2[0] not in orig and r3[0] not in orig:
    print("Invalid rules")
    done = True
if len(inp) != len(fin):
    print("Invalid lengthed final")
    done = True
if lim < 0:
    print("Invalid length")
    done = True

for i in range(lim):
    if done: break
    for j in range(lim):
        if done: break
        for k in range(lim):
            for x in range(k):
                orig = orig.replace(r1[0], r1[1])
            for y in range(j):
                orig = orig.replace(r2[0], r2[1])
            for z in range(i):
                orig = orig.replace(r3[0], r3[1])
            #print k, j, i, orig
            if orig == fin:
                stp = 1
                print "1\t" + inp
                for a in range(k):
                    stp += 1
                    inp = inp.replace(r1[0], r1[1])
                    print str(stp) + "\t" + inp
                for b in range(j):
                    stp += 1
                    inp = inp.replace(r2[0], r2[1])
                    print str(stp) + "\t" + inp
                for c in range(i):
                    stp += 1
                    inp = inp.replace(r3[0], r3[1])
                    print str(stp) + "\t" + inp
                done = True
                break
            else:
                orig = inp
if not done:
    print("Impossible")