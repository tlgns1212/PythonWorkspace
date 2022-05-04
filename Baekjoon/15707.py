import sys
a, b, r = map(int, sys.stdin.readline().split())
if a*b > r:
    print('overflow')
else:
    print(a*b)
