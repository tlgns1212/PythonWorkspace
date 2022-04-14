import sys
N = int(sys.stdin.readline())
A = []
max = 0
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort(reverse=False)
for i in range(N):
    if max < A[i] * (N-i):
        max = A[i] * (N-i)
print("{0}".format(max))
