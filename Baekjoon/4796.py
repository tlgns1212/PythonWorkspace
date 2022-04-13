import sys
i = 1
while(1):
    A = list(map(int, sys.stdin.readline().split()))
    if A[0] == 0 and A[1] == 0 and A[2] == 0:
        break
    div = A[2]//A[1]
    rest = A[2] % A[1] if (A[2] % A[1]) < A[0] else A[0]
    answer = div*A[0] + rest
    print("Case {0}: {1}".format(i, answer))
    i += 1
