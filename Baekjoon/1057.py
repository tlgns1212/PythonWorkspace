import sys
N, first, second = map(int, sys.stdin.readline().split())
start = 2
count = 1
while(1):
    if first <= start and second <= start:
        while(1):
            start /= 2
            if first//(start+0.0001) == second//(start+0.0001):
                count -= 1
            else:
                break
        break
    start *= 2
    count += 1
print(count)
