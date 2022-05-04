T = int(input())
for _ in range(T):
    N = int(input())
    scores = [0 for _ in range(101)]
    students = list(map(int, input().split()))
    max = 0
    maxIndex = 0
    for student in students:
        scores[student] += 1
    for i in range(len(scores)):
        if max <= scores[i]:
            max = scores[i]
            maxIndex = i
    print("#{} {}".format(N, maxIndex))
