T = int(input())
N = int(input())
for t in range(T):
    print("#{}".format(t+1))
    answer = []                     # 정답을 담아야 함
    for i in range(N):
        temp = []                   # 파스칼의 한 줄
        for j in range(i+1):
            if j == 0 or j == i:    # 한 줄에서 첫번째 혹은 마지막은 무조건 1
                temp.append(1)
            else:
                # i-1, 즉 이전 줄의 두개를 합친게 이번 줄의 숫자가 됨
                temp.append(answer[i-1][j] + answer[i-1][j-1])
        answer.append(temp)
    for i in answer:
        # asterisk를 사용하는 방법 중 하나로 리스트 안의 내용만 빼다 쓸 수 있다.
        print(*i)
