N = int(input())
counter = 0
for i in range(N):
    if (int(input()) * 5 - int(input()) * 3) > 40:
        counter += 1
print(str(counter) + ('+' if counter == N else ''))