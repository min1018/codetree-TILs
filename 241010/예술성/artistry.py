from collections import deque 
from collections import defaultdict 
from itertools import combinations 

def bfs(i, k, groupCnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((i, k))
    new[i][k] = groupCnt
    visited[i][k] = 1
    # 그룹속의 수, 칸 개수, 인접한 변 수 
    near = [[0] * n for _ in range(n)]
    
    total = 1
    while q:
        x, y = q.popleft()
        for h in range(4):
            nx, ny = x + dx[h], y + dy[h]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    if board[nx][ny] == board[i][k]: #같은 그룹 
                        q.append((nx, ny))
                        total += 1
                        new[nx][ny] = groupCnt
                        visited[nx][ny] = 1
    
    return (board[i][k], total)
# 생각치 못한 부분, 1 블록이 여러개임 

def getNear(i, k, new):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dic = defaultdict(int)
    q = deque()
    q.append((i, k))
    visited[i][k] = 1

    check = [[0] * n for _ in range(n)]
    while q:
        x, y = q.popleft()  
        for h in range(4):
            nx, ny = x + dx[h], y + dy[h]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == board[i][k] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif board[nx][ny] != board[i][k]:
                    dic[new[nx][ny]] += 1
                    #visited[nx][ny] = 1
    return (new[i][k], dic)    

def rotate90(sx, sy, length):
    new = [[0] * length for _ in range(length)]
    for x in range(sx, sx+length):
        for y in range(sy, sy+length):
            ox, oy = x - sx, y - sy
            rx, ry = oy, length-1-ox
            new[rx][ry] = board[x][y]

    for i in range(length):
        for k in range(length):
            board[i+sx][k+sy] = new[i][k]


def rotateX():
    new = [[0] * n for _ in range(n)]
    for i in range(n):
        new[n-1-i][n//2] = board[n//2][i]
    for i in range(n):
        new[n//2][i] = board[i][n//2]

    for i in range(n):
        board[i][n//2] = new[i][n//2]
        board[n//2][i] = new[n//2][i]

def rotate():
    rotateX()
    rotate90(0, 0, n//2)
    rotate90(0, n//2+1, n//2)
    rotate90(n//2+1, 0, n//2)
    rotate90(n//2+1, n//2+1, n//2)

def calcScore(a, b):
    anum, atotal, adic = group[a]
    bnum, btotal, bdic = group[b]
    return (atotal+btotal) * anum * bnum * adic[b]

n = int(input())
board = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
ans = 0

for i in range(4):
    visited = [[0] * n for _ in range(n)]
    new = [[0] * n for _ in range(n)]
    if i != 0:
        rotate()

    groupCnt = 1
    group = []
    group.append([])
    for i in range(n):
        for k in range(n):
            if visited[i][k] == 0:
                num, total = bfs(i, k, groupCnt)
                groupCnt += 1
                group.append([num, total])
    
    #print(new)
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if visited[i][k] == 0:
                idx, dic = getNear(i, k, new)
                group[idx].append(dic)


    groups = len(group)
    #print(group)
    nums = [i for i in range(1, groups)]
    # 그룹으로2개로 조합 구해서 점수 계산 

    cases = list(combinations(nums, 2))
    for a, b in cases:
        ans += calcScore(a, b)

print(ans)