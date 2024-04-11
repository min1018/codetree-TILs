import time
from collections import deque


def getBase(idx):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tx, ty = player[idx]
    base = []
    for i in range(n):
        for k in range(n):
            if graph[i][k] == 1:
                base.append([i, k, 0])
    poss = []
    for h in range(len(base)):
        q = deque()
        x, y, cnt = base[h][0], base[h][1], base[h][2]
        q.append([x, y, cnt])
        visited = [[0] * n for _ in range(n)]
        visited[x][y] = 1
        while q:
            cx, cy, cnt = q.popleft()
            for j in range(4):
                nx = cx + dx[j]
                ny = cy + dy[j]
                if 0 <= nx < n and 0 <= ny < n:
                    if (tx, ty) == (nx, ny):
                        poss.append([x, y, cnt + 1])
                        break
                    if graph[nx][ny] != -1 and visited[nx][ny] == 0:
                        q.append([nx, ny, cnt + 1])
                        visited[nx][ny] = 1
    poss.sort(key=lambda x: (x[2], x[0], x[1]))
    return poss[0][0], poss[0][1]


def getNext(idx, cx, cy):
    tx, ty = player[idx]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    q = deque()
    poss = []
    visited = [[0] * n for _ in range(n)]
    visited[cx][cy] = 1
    for a in range(4):
        nx = cx + dx[a]
        ny = cy + dy[a]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] != -1:
                if (nx, ny) == (player[idx][0], player[idx][1]):
                    return nx, ny
                q.append((nx, ny, nx, ny, 1))
                visited[nx][ny] = 1
    while q:
        x, y, ix, iy, cnt = q.popleft()
        for h in range(4):
            nx = x + dx[h]
            ny = y + dy[h]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != -1 and visited[nx][ny] == 0:
                    if (tx, ty) == (nx, ny):
                        poss.append((ix, iy, cnt + 1))
                        visited[nx][ny] = 1
                        break
                    visited[nx][ny] = 1
                    q.append((nx, ny, ix, iy, cnt + 1))

    poss.sort(key=lambda x: (x[2], x[0], x[1]))
    return poss[0][0], poss[0][1]


n, mem = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
player = []
for i in range(mem):
    x, y = map(int, input().split())
    player.append([x - 1, y - 1])

curr = [[] for _ in range(mem)]
change = []
ans = 0
T = 0

while True:
    T += 1
    if T - 1 < mem:
        x, y = getBase(T - 1)
        curr[T - 1] = [x, y]
        change.append((x, y))
    for i in range(len(curr)):
        if len(curr[i]) > 0 and i != T - 1:
            cx, cy = curr[i]
            if (cx, cy) != (player[i][0], player[i][1]):
                nx, ny = getNext(i, cx, cy)
                curr[i] = [nx, ny]
                if (nx, ny) == (player[i][0], player[i][1]):
                    ans += 1
                    change.append((nx, ny))
    for ax, ay in change:
        graph[ax][ay] = -1
    if ans == mem:
        print(T)
        break