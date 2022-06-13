def bfs(x, y):
    check = 0
    temp = [[x, y]]                                     # 시작지점을 temp에 넣고
    visited[x][y] = 1                                   # 시작지점의 방문여부 True

    while True:
        # 스택이라고 생각하고 FILO(First in last out)
        i, j = temp.pop()

        for dir in range(4):                            # 상하좌우 네 가지 방향에 따라 반복
            ni = i + directionX[dir]
            nj = j + directionY[dir]

            if 0 <= ni < 100 and 0 <= nj < 100:           # maze의 크기를 벗어나지 않도록
                if maze[ni][nj] == 0 and visited[ni][nj] == 0:  # 방문한적이 없고 길이 있으면 해당 길을 temp에 저장
                    temp.append([ni, nj])
                    visited[ni][nj] = 1
                elif maze[ni][nj] == 3:                 # 출구면 break
                    check = 1
                    break
        if check == 1 or len(temp) == 0:
            break
    return check


directionX = [-1, 1, 0, 0]
directionY = [0, 0, -1, 1]

for t in range(10):                                     # 여기가 시작점
    nothing = input()                                   # 필요없는 숫자 하나 입력받아주고
    maze = [list(map(int, input()))for _ in range(100)]  # 100줄의 미로를 maze에 저장
    visited = [[0]*100 for _ in range(100)]               # 방문 여부도 100*100으로 만들기

    x = -1                                              # 시작지점 찾기
    y = -1

    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                x = i
                y = j
                break
        if x != -1:
            break
    answer = bfs(x, y)                                  # 너비우선탐색 시작
    print("#{} {}".format(t+1, answer))
