import sys
l, d, n = map(int, sys.stdin.readline().split())
birds = []
answer = 0
for _ in range(n):
    birds.append(int(sys.stdin.readline()))
birds.sort()
if len(birds) > 0:
    small = birds[0] - 6
    big = (l-6) - birds[-1]
    answer += small//d
    answer += big//d
    for i in range(1, len(birds)-1):
        diff = birds[i+1] - birds[i]
        answer += ((diff//d)-1)
else:
    answer = (((l-6) - (6)) // d) + 1
print(answer)
