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
    # print("every possible base for", idx, base)
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
                    if graph[nx][ny] != -1 and visited[nx][ny] == 0 and (nx, ny) not in change:
                        q.append([nx, ny, cnt + 1])
                        visited[nx][ny] = 1
    poss.sort(key=lambda x: (x[2], x[0], x[1]))
    return poss[0][0], poss[0][1]


def getNext(idx, cx, cy):
    # print("idx", idx)
    tx, ty = player[idx]
    q = deque()
    q.append((cx, cy, -1, -1))
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[0] * n for _ in range(n)]
    while q:
        x, y, ix, iy = q.popleft()
        for h in range(4):
            nx = x + dx[h]
            ny = y + dy[h]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1 and visited[nx][ny] == 0 and (nx, ny) not in change:
                # 범위 안, 방문 가능한 지역 
                if (nx, ny) == (tx, ty):
                    if ix == -1 and iy == -1:
                        return nx, ny
                    else: 
                        return ix, iy 
                elif ix == -1 and iy == -1: # 방문 첨해서 초기 위치가 저장 안돈 경우 
                    q.append((nx, ny, nx, ny))
                    visited[nx][ny] = 1
                else:
                    q.append((nx, ny, ix, iy))
                    visited[nx][ny] = 1
                


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
    # print("t", T)
    # print("start graph", graph)
    again = []
    for i in range(len(curr)):
        if len(curr[i]) > 0:
            cx, cy = curr[i]
            if (cx, cy) != (player[i][0], player[i][1]):
                nx, ny = getNext(i, cx, cy)
                if (nx, ny) == (player[i][0], player[i][1]):
                    ans += 1
                    curr[i] = [nx, ny]
                    change.append((nx, ny))
                else:
                    again.append(i)
    if len(again) > 0:
        for idx in again:
            x, y = curr[idx]
            nx, ny = getNext(idx, x, y)
            curr[idx] = [nx, ny]

    # base 찾기 
    if T - 1 < mem:
        x, y = getBase(T - 1)
        curr[T - 1] = [x, y]
        change.append((x, y))
    for ax, ay in change:
        graph[ax][ay] = -1
    # print("curr ans", ans)
    # print("curr", curr)
    # print("graph", graph)
    if ans == mem:
        print(T)
        break