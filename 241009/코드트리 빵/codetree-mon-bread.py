from collections import deque 

def get_minDist(sx, sy, tx, ty):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0] # 북 서 동 남 우선 조건 충족 

    q = deque()
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = -1
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != -1:
            if nx == tx and ny == ty:
                return (nx, ny, 1)
            visited[nx][ny] = 1
            q.append((nx, ny, nx, ny, 1))

    while q:
        x, y, mx, my, cnt = q.popleft()
        #print(x, y, mx, my, cnt)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and board[nx][ny] != -1:
                    visited[nx][ny] = 1
                    if nx == tx and ny == ty:
                        return (mx, my, cnt + 1) # 첫번째 이동 좌표 반환 
                    q.append((nx, ny, mx, my, cnt + 1))



def base_camp(idx, i, k):
    # print("goal", i, k)
    poss = []
    for x, y in camp:
        if board[x][y] == -2: # 추후 방문 못하는 베이스캠프는 -1로 변경 
            nx, ny, dist = get_minDist(x, y, i, k)
            poss.append((x, y, dist))
            # print("check", x, y, nx, ny, dist)
    poss.sort(key = lambda x : (x[2], x[0], x[1]))
    # print("poss", poss)
    return (poss[0][0], poss[0][1])


n, m = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(n)]
camp = []
for i in range(n):
    for k in range(n):
        if board[i][k] == 1:
            board[i][k] = -2
            camp.append([i, k])


goal = []
for _ in range(m):
    i, k = map(int, input().rstrip().split(" "))
    goal.append([i-1, k-1])

cnt = 0 #도착한 사람 수 카운트 
time = 1
onMap = [[] for _ in range(m)]
while cnt < m:
    #print(time)
    nxtRed = []
    for i in range(m):
        if len(onMap[i]) == 2:
            x, y = onMap[i]
            nx, ny, dist = get_minDist(x, y, goal[i][0], goal[i][1])
            if nx == goal[i][0] and ny == goal[i][1]:
                nxtRed.append((goal[i][0], goal[i][1]))
                cnt += 1
                onMap[i] = [1]
            else:
                onMap[i] = [nx, ny]

    if time <= len(goal):
        x, y = base_camp(time-1, goal[time-1][0], goal[time-1][1])
        onMap[time-1] = [x, y]
        nxtRed.append((x, y))
    
    for x, y in nxtRed:
        board[x][y] = -1
    #print(board)
    time += 1


print(time-1)