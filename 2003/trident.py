l, s, h, gap, gap2 = "", "", "", "", ""

while True:
    try:
        l = raw_input("Insert the length: ")
        l = int(l)
    except ValueError:
        print "Invalid length ({}). Please try again.".format(l)
    else:
        break

while True:
    try:
        s = raw_input("Insert the gap length: ")
        s = int(s)
    except ValueError:
        print "Invalid gap length ({}). Please try again.".format(s)
    else:
        break

while True:
    try:
        h = raw_input("Insert handle length: ")
        h = int(h)
    except ValueError:
        print "Invalid handle length ({}). Please try again.".format(h)
    else:
        break

for i in range(s):
    gap += " "

for i in range(s + 1):
    gap2 += " "

for i in range(l):
    print "*{}*{}*".format(gap, gap)

print "*" * (2 * len(gap) + 3)

for i in range(h):
    print gap2 + "*"