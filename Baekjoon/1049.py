import sys
N, M = map(int, sys.stdin.readline().split())
pack = []
one = []
for i in range(M):
    a = list(map(int, sys.stdin.readline().split()))
    pack.append(a[0])
    one.append(a[1])
pack.sort()
one.sort()
if one[0]*6 < pack[0]:
    pack[0] = one[0]*6
N_div = N % 6
N = N//6
if N_div * one[0] > pack[0]:
    print((N+1)*pack[0])
else:
    print(N*pack[0] + N_div*one[0])
