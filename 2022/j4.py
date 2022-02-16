x = []
for i in range(int(input())):
    x.append(input().split())
y = []
for i in range(int(input())):
    y.append(input().split())
g = []
for i in range(int(input())):
    g.append(input().split())

vio = 0

for i in range(len(g)):
    j = 0
    while j < len(x):
        if (x[j][0] in g[i]) ^ (x[j][1] in g[i]):
           vio += 1
           del x[j]
           j -= 1
        j += 1
    j = 0
    while j < len(y):
        if (y[j][0] in g[i]) and (y[j][1] in g[i]):
           vio += 1
           del y[j]
           j -= 1
        j += 1

print(vio)