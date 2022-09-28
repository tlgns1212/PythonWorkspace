import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
count = 0
B = [0 for _ in range(N)]
for now in range(1001):
    for i in range(len(A)):
        if now == A[i]:
            B[i] = count
            count += 1
for i in B:
    print(i, end=" ")
