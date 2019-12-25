start = raw_input("Insert a starting coordinate: ").split(" ")
end = raw_input("Insert a destination coordinate: ").split(" ")
total = int(raw_input("Insert a total number of trips: "))
start = [int(i) for i in start]
end = [int(i) for i in end]

xDiff = abs(start[0] - end[0])
yDiff = abs(start[1] - end[1])

#print xDiff, "+", yDiff, "<=", total

if xDiff + yDiff <= total:
    if xDiff % 2: xDiff = 1
    else: xDiff = 0
    if yDiff % 2: yDiff = 1
    else: yDiff = 0

    if total % 2 == 0:
        #print "Total is even"
        if xDiff == yDiff:
            print "Y"
        else:
            print "N"
    elif total % 2 != 0:
        #print "Total is odd"
        if xDiff != yDiff:
            print "Y"
        else:
            print "N"
else:
    print "N"

# 4 4
# 4 3
# 3
# 4 - 4 = 0
# 4 - 3 = 1
# 0 1 (0 + 1 <= 3) (0 = Even, 1 = Odd, Even + Odd = Odd, 3 = Odd)
# Y
# Proof: (4 4): 4 3, 5 3, 4 3

# 2 5
# 7 3
# 4
# 2 - 7 = -5
# 5 - 3 = 2
# -5 2 (5 + 2 >= 4)
# N

# 3 4
# 2 2
# 5
# 3 - 2 = 1
# 4 - 2 = 2
# 1 2 (1 + 2 <= 5) (1 = Odd, 2 = Even, Odd + Even = Odd, 5 = Odd
# Y
# Proof: (3 4): 3 3, 2 3, 3 3, 2 3, 2 2