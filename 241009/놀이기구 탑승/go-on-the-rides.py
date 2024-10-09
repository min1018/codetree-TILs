def bfs(curr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    poss = []
    for i in range(n):
        for k in range(n):
            if board[i][k] == 0: #공석인 경우 주변 탐색 시작 
                blank = 0 #주변 공석
                friend = 0 #친구
                for h in range(4):
                    nx, ny = i+dx[h], k+dy[h]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 0:
                            blank += 1
                        elif board[nx][ny] in like[curr]:
                            friend += 1
                poss.append([friend, blank, i, k]) # 친구, 공석, 행, 열 
    poss.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    # 앉을 수 있는 자리가 없는 경우가 존재하는가? 아니요 
    board[poss[0][2]][poss[0][3]] = curr
    return 
            


def score():
    point = [0, 1, 10, 100, 1000]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0
    for i in range(n):
        for k in range(n):
            curr = board[i][k]
            cnt = 0
            for h in range(4):
                nx, ny = i+dx[h], k+dy[h]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in like[curr]:
                        cnt += 1
            ans += point[cnt] 
    return ans 


n = int(input())
board = [[0] * n for _ in range(n)]
like = [[] for _ in range(n*n+1)]
turn = []
for _ in range(n*n):
    p, a, b, c, d = map(int, input().split(" "))
    like[p] = [a, b, c, d]
    turn.append(p)

for stu in turn:
    bfs(stu)
print(score())