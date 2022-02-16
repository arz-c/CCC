minX = minY = float("Infinity")
maxX = maxY = float("-Infinity")

for i in range(int(raw_input())):
    x, y = [int(i) for i in raw_input().split(',')]
    
    if x < minX: minX = x
    if x > maxX: maxX = x
    if y < minY: minY = y
    if y > maxY: maxY = y

print str(minX - 1) + ',' + str(minY - 1) + '\n' + str(maxX + 1) + ',' + str(maxY + 1)