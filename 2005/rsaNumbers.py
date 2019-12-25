# 4 divisors = rsa num
low = int(raw_input("Insert the lower limit of the range: "))
hi = int(raw_input("Insert the upper limit of the range: "))
count = 2
total = 0

for i in range(low, hi + 1):
    count = 2
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            count += 1
    if count == 4:
        #print i
        total += 1

print total