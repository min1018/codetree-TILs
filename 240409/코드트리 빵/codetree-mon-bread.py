from collections import deque
import time

flag = 0


def chooseBase(i):  # i번째 맴버
    global flag
    # print("pt",target[i][0])
    if not q:
        flag = -1
        return -1, -1, -1
    t = q.popleft()
    tx, ty = t[0], t[1]
    if Time > i + 1:  # t <= m
        return -1, -1, -1
    options = []
    for k in range(len(base)):
        # print("k", k)
        bx, by = base[k][0], base[k][1]
        if graph[bx][by] == 1:
            dist = abs(tx - bx) + abs(ty - by)
            options.append([dist, bx, by])
    options.sort(key=lambda x: (x[0], x[1], x[2]))
    #print("options", options)
    return options[0][0], options[0][1], options[0][2]


def moveStore(x, y, num):
    global cnt
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    options = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            #print("target tx ty", target)
            if nx == target[num][0] and ny == target[num][1]:
                cnt += 1
                curr[num] = []
                return nx, ny
            dist = abs(nx - target[num][0]) + abs(ny - target[num][1])
            options.append([dist, nx, ny])
    options.sort(key=lambda x: (x[0], x[1], x[2]))
    return options[0][1], options[0][2]


n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
target = []
base = []
for i in range(n):
    for k in range(n):
        if graph[i][k] == 1:
            base.append([i, k])

for i in range(m):
    x, y = map(int, input().split(" "))
    target.append([x - 1, y - 1])
#print("target", target)
q = deque(target)
Time = 0
cnt = 0
curr = [[] for _ in range(m)]
while True:
    if cnt == m:  # 모두 편의점 속
        break
    Time += 1
    k = Time -1
    #print("time", Time)
    if flag == 0:
        dist, bx, by = chooseBase(k)
        #print("dist bx by ", dist, bx, by)
    nx, ny = -1, -1
    for i in range(m):
        if len(curr[i]) > 0:
            x, y = curr[i][0], curr[i][1]
            nx, ny = moveStore(x, y, i)
            if len(curr[i]) != 0:  # 도착하지 않은 경우
                curr[i] = [nx, ny]
                nx, ny = -1, -1

    if bx != -1 and by != -1:
        curr[k] = [bx, by]
        graph[bx][by] = -1
    if nx != -1 and ny != -1:
        graph[nx][ny] = -1
    #print("target", target)
    #print("curr", curr)
    #print(cnt)

print(Time)