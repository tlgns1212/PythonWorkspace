import sys
N = (sys.stdin.readline())
basic = N[0]
count = 0
for i in N:
    if basic != i:
        count += 1
        basic = i
print(count//2)
