import sys
score = []
for i in range(8):
    score.append([int(sys.stdin.readline()), i])
score.sort(reverse=True)
answer = []
all = 0
for i in range(5):
    answer.append(score[i][1])
    all += score[i][0]
answer.sort()
print("{0}\n{1} {2} {3} {4} {5}".format(
    all, answer[0]+1, answer[1]+1, answer[2]+1, answer[3]+1, answer[4]+1))
