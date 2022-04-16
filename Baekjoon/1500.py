import sys
S, K = map(int, sys.stdin.readline().split())
temp = S//K
max = 1
used = 0
skipped = 0
if S/K == S//K:
    for _ in range(K):
        max *= temp
else:
    for i in range(K):
        if (K-i)*(temp+1) == S-used:
            skipped = K-i
            break
        used += temp
        max *= temp
    if skipped != 0:
        for _ in range(skipped):
            max *= (temp+1)
print(max)
