import sys
N, K = map(int, sys.stdin.readline().split())
days = list(map(int, sys.stdin.readline().split()))
max = -101
for i in range(N-K+1):
    temp_max = 0
    for j in range(K):
        temp_max += days[i+j]
    if temp_max > max:
        max = temp_max
print(max)
