T = int(input())
for a in range(T):
    N = int(input())
    snailList = [[0 for _ in range(N)] for _ in range(N)]
    # 0 = right, 1 = down, 2 = left, 3 = up
    direction = 0
    now = 2
    i = 0
    j = 0
    snailList[0][0] = 1
    if N == 1:
        print("#{}".format(a+1))
        print(1)
    else:
        while(1):
            if direction == 0:
                j += 1
                if j < N and snailList[i][j] == 0:
                    snailList[i][j] = now
                    now += 1
                else:
                    j -= 1
                    direction += 1
                    if snailList[i+1][j] != 0:
                        break
            elif direction == 1:
                i += 1
                if i < N and snailList[i][j] == 0:
                    snailList[i][j] = now
                    now += 1
                else:
                    i -= 1
                    direction += 1
                    if snailList[i][j-1] != 0:
                        break
            elif direction == 2:
                j -= 1
                if j >= 0 and snailList[i][j] == 0:
                    snailList[i][j] = now
                    now += 1
                else:
                    j += 1
                    direction += 1
                    if snailList[i-1][j] != 0:
                        break
            else:
                i -= 1
                if i >= 0 and snailList[i][j] == 0:
                    snailList[i][j] = now
                    now += 1
                else:
                    i += 1
                    direction = 0
                    if snailList[i][j+1] != 0:
                        break
        print("#{}".format(a+1))
        for x in snailList:
            for y in x:
                print(y, end=" ")
            print()
