import sys
T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    c = []
    answer = 0
    for _ in range(n):
        c.append(list(map(int, sys.stdin.readline().split())))
    for i in c:
        firstx = x1 - i[0]
        firsty = y1 - i[1]
        secondx = x2 - i[0]
        secondy = y2 - i[1]
        first = firstx*firstx + firsty*firsty
        second = secondx*secondx + secondy*secondy
        c2 = int(i[2]) * int(i[2])
        if first < c2:
            if second < c2:
                answer += 0
            else:
                answer += 1
        else:
            if second < c2:
                answer += 1
            else:
                answer += 0
    print("!!!")
    print(answer)
