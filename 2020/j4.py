wholeStr = raw_input()
subStr = raw_input()

found = False
for i in range(len(wholeStr) - len(subStr) + 1):
    curStr = wholeStr[i:len(subStr) + i]
    for char in wholeStr[i:len(subStr) + i]:
        if curStr == subStr:
            found = True
            break
        else:
            curStr += curStr[0]
            curStr = curStr[1:]
    if found:
        break

if found:
    print "yes"
else:
    print "no"
