
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    letters = input().strip()
    sideNum = N//4
    madeNum = []
    for l in range(sideNum):
        for j in range(4):
            tempNum = []
            for k in range(sideNum, 0, -1):
                tempNum.append(letters[(j*sideNum-k-l)])
            tempStr = "".join(tempNum)
            if tempStr not in madeNum:
                madeNum.append(tempStr)
    madeNum.sort(reverse=True)
    print("#{} {}".format(i+1, int(madeNum[K-1], 16)))
