import copy
from collections import deque

ans = 0

def growth():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for k in range(n):
            if graph[i][k] > 0 and graph[i][k] != 9999999:  # 현재 위치가 나무일 경우
                for h in range(4):
                    nx = i + dx[h]
                    ny = k + dy[h]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] > 0 and graph[nx][ny] != 9999999:
                            graph[i][k] += 1
            elif graph[i][k] < 0:
                graph[i][k] += 1
                # 제초제 뿌린지 1년 지남


def spread():
    spreading = [[0] * n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for k in range(n):
            cnt = 0
            temp = []
            if graph[i][k] > 0 and graph[i][k] != 9999999: # 나무인 칸에서
                for h in range(4):
                    nx = i + dx[h]
                    ny = k + dy[h]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 0:
                            cnt += 1
                            temp.append((nx, ny))
                if cnt > 0:
                    feed = graph[i][k] // cnt
                    for x, y in temp:
                        spreading[x][y] += feed
    for i in range(n):
        for k in range(n):
            graph[i][k] += spreading[i][k]


def choosePoison(length):
    # print("length", length)
    dx = [-1, -1, 1, 1]
    dy = [1, -1, 1, -1]
    best = -1
    poss = []
    for i in range(n):
        for k in range(n):
            if graph[i][k] > 0 and graph[i][k] != 9999999:
                q = deque()
                q.append((i, k))
                visited = [[0] * n for _ in range(n)]
                cnt = graph[i][k]
                for h in range(4):
                    q.append((i, k))
                    while q:
                        x, y = q.popleft()
                        nx = x + dx[h]
                        ny = y + dy[h]
                        if i - length <= nx <= i + length and k - length <= ny <= k + length:
                            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                                if graph[nx][ny] >= 0 and graph[nx][ny] != 9999999:
                                    visited[nx][ny] = 1
                                    if graph[nx][ny] != 0:
                                        q.append((nx, ny))
                                    #print(graph[nx][ny])
                                    cnt += graph[nx][ny]

                # print("poison cnt",i, k, cnt)
                best = max(best, cnt)
                poss.append((cnt, i, k))
    poss.sort(key=lambda x: (-x[0], x[1], x[2]))
    #print("poss", poss)
    return poss[0][1], poss[0][2]


def spreadPoison(px, py, length):
    global ans
    #print("before spreading poison", graph)
    dx = [-1, -1, 1, 1]
    dy = [1, -1, 1, -1]
    visited = [[0] * n for _ in range(n)]
    ans += graph[px][py]
    graph[px][py] = -c-1
    for h in range(4):
        q = deque()
        q.append((px, py))
        while q:
            x, y = q.popleft()
            nx = x + dx[h]
            ny = y + dy[h]
            if px - length <= nx <= px + length and py - length <= ny <= py + length:
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    if graph[nx][ny] >= 0 and graph[nx][ny] != 9999999:
                        if graph[nx][ny] > 0:
                            #print("dead", graph[nx][ny])
                            ans += graph[nx][ny]
                        visited[nx][ny] = 1
                        graph[nx][ny] = -c-1
                        q.append((nx, ny))


n, year, l, c = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

# 벽을 문자로
for i in range(n):
    for k in range(n):
        if graph[i][k] == -1:
            graph[i][k] = 9999999

for _ in range(year):
    growth()
    #print("after growth", graph)
    spread()
    #print("after spread", graph)
    px, py = choosePoison(l)
    #print("px, py", px, py)
    spreadPoison(px, py, l)
    #print("after poison", graph)

print(ans)