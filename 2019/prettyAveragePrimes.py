def isPrime(num):
    if num == 1 or num == 2:
        return True
    for i in range(2, num // 2):
        if(num % i) == 0:
            return False
    return True

def findNums(i):
    for j in range(1, i * 2 + 1):
        if not isPrime(j):
            continue
        for k in range(1, i * 2):
            if not isPrime(k):
                continue
            if (j + k) / 2 == i:
                return str(j) + " " + str(k)

def test():
    for i in range(2, 1000):
        print findNums(i)

tot = int(raw_input("Insert total: "))
inps = []
for i in range(tot):
    inps.append(int(raw_input("Insert #{}: ".format(i + 1))))

for i in inps:
    print findNums(i)