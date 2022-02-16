rows = int(raw_input())
cols = int(raw_input())

room = []
for i in range(rows):
    newRow = [int(j) for j in raw_input().split(' ')]
    room.append(newRow)

def checkSpot(spot, completed):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            # print room[i][j]
            if i * j == spot and [i, j] not in completed:
                # print 'i', i, 'j', j
                completed.append([i, j])
                # print 'completed', completed
                if (i == rows and j == cols) or checkSpot(room[i - 1][j - 1], completed):
                    # print 'found enterance'
                    return True           
    return False

if checkSpot(room[0][0], []):
    print "yes"
else:
    print "no"