room = []
#for i in range(int(raw_input())):
#    for j in range(int(raw_input())):
#        room[i][j] = int(raw_input())

room = [
    [3, 10, 8, 14],
    [1, 11, 12, 12],
    [6, 2, 3, 9]
]

def canJump(cur, options, completed):
    for i in range(1, len(room) + 1):
        for j in range(1, len(room[0]) + 1):
            #print 'i', i, 'j', j, 'i*j', i * j, 'cur', cur
            if i * j == cur:
                if [i, j] not in options:
                    options.append([i, j])
                    #print "new options", options
    #print 'completed', completed
    #print 'options', options
    for option in options:
        #print 'loopOption', option
        if option not in completed:
            completed.append(option)
            canJump(room[option[0] - 1][option[1] - 1], options, completed)
    return options

found = False
for i in range(len(room)):
    for j in range(len(room[0])):
        #print "spot", room[i][j]
        #print 'xi', i, 'xj', j
        for option in canJump(room[i][j], [], []):
            if option == [len(room) + 1, len(room[0]) + 1]:
                found = True
if found:
    print "yes"
else:
    print "no"
            
