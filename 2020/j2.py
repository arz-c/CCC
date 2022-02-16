maxInfected = int(raw_input())
curInfected = int(raw_input())
spread = int(raw_input())

day = 0
while curInfected <= maxInfected:
    curInfected += curInfected * spread
    day += 1

print day
