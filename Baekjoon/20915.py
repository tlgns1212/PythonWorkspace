import sys
T = int(sys.stdin.readline())
for _ in range(T):
    b = 0
    n = list(map(int, sys.stdin.readline().rstrip()))
    zeros = n.count(0)
    for i in range(len(n)):
        if n[i] == 6:
            n[i] = 9
    n.sort(reverse=True)
    for i in range(zeros):
        n.pop()
    if not(n):
        print(0)
        continue
    a = n[0]
    for i in range(1, len(n)):
        if a > b:
            b = b*10 + n[i]
        else:
            a = a*10 + n[i]
    for i in range(zeros):
        a *= 10
    print(a*b)
