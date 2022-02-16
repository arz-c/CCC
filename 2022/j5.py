N = int(input())
T = int(input())
map = [[0 for i in range(N)] for j in range(N)]
for i in range(T):
    r, c = [(int(e) - 1) for e in input().split()]
    map[r][c] = 1

def largestSquareAt(r, c):
    for i in range(r, N):

largestSquareSL = -1

for c in range(N - 1):
    sl = largestSquareAt(0, c)
    if sl > largestSquareSL:
        largestSquareSL = sl

for r in range(N - 1):
    sl = largestSquareAt(r, N - 1)
    print(sl, largestSquareSL, r, N - 1)
    if sl > largestSquareSL:
        largestSquareSL = sl

for c in range(N - 1, -1, -1):
    sl = largestSquareAt(N - 1, c)
    if sl > largestSquareSL:
        largestSquareSL = sl

for r in range(N - 1, -1, -1):
    sl = largestSquareAt(r, 0)
    if sl > largestSquareSL:
        largestSquareSL = sl

print(largestSquareSL)