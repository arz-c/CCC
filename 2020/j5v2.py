rows = int(raw_input())
cols = int(raw_input())

room = []
for i in range(rows):
    room.append([])
    newRow = raw_input().split(' ')
    for j in range(len(newRow)):
        room[i].append([])
        room[i][j] = int(newRow[j])

def checkSpot(spot, completed):
    for i in range(rows):
        for j in range(cols):
            # print room[i][j]
            if (i + 1) * (j + 1) == spot and [i, j] not in completed:
                # print 'i', i, 'j', j
                completed.append([i, j])
                # print 'completed', completed
                if (i == 0 and j == 0) or checkSpot(room[i][j], completed):
                    # print 'found enterance'
                    return True           
    return False

if checkSpot(room[rows - 1][cols - 1], []):
    print "yes"
else:
    print "no"
