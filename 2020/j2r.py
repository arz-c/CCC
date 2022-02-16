maxInfected = int(raw_input())
totalInfected = int(raw_input())
spread = int(raw_input())

day = 0
curSpreading = totalInfected
while totalInfected <= maxInfected:
    curSpreading *= spread
    totalInfected += curSpreading
    day += 1

print day
