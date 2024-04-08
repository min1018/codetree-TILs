from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
flag = 0

# 최단거리 순으로 움직이나, 실제 이동거리는 무조건 1임 이 부분 망각
def move():
    # 최단거리: 직접 구함, 상하우선 : 상하 부터 이동하여 보장
    global ans
    global flag
    participant = deque()
    door = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 10:
                participant.append((x, y))
            elif graph[x][y] == -1:
                door = ((x, y))
    if len(participant) == 0:
        flag = -1
    for i in participant:
        x, y = i[0], i[1] # 찝
        standard = abs(door[0] - x) + abs(door[1] - y) # 원래 거리보다 가까워야
        temp = []
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0<= ny < n and graph[nx][ny] <= 0: # 탈출할 수도 있으니 <=
                if nx == door[0] and ny == door[1]: # 탈출
                    graph[x][y] = 0
                    ans += 1
                    break
                temp.append((nx, ny, abs(door[0]-nx) + abs(door[1]-ny)))
        if len(temp) != 0:
            temp.sort(key = lambda x: (x[2]))
            tx, ty, dist = temp[0]
            if dist != 0 and dist < standard:
                graph[tx][ty] = 10
                graph[x][y] = 0
                ans += 1

def getSquare():
    # 크기, x 작은, y 작은 순
    participant = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 10:
                participant.append((x, y))
            elif graph[x][y] == -1:
                door = ((x, y))
    poss = []
    for i in participant:
        px, py = i[0], i[1]
        dx, dy = door[0], door[1]
        length = max(abs(px-dx), abs(py-dy))
        tx, ty = max(dx, px), max(dy, py)
        if tx - length >= 0:
            tx = tx - length
        else:
            tx = 0
        if ty - length >= 0:
            ty = ty - length
        else:
            ty = 0
        poss.append((length + 1, tx, ty))
    poss.sort(key = lambda x: (x[0], x[1], x[2]))
    return poss[0]


def turn(length, sx, sy):
    temp = [[0]* n for _ in range(n)]
    for i in range(sx, sx+length):
        for k in range(sy, sy+length):
            ox, oy = i - sx , k - sy
            #tx, ty = length - ox -1, oy
            tx, ty = oy, length - ox - 1
            temp[sx + tx][sy + ty] = graph[i][k]
    for i in range(sx, sx+length):
        for k in range(sy, sy+length):
            if 0 < temp[i][k] < 10: # 출구, 빈칸 아니고 사람 아니면
                graph[i][k] = temp[i][k]-1
            else:
                graph[i][k] = temp[i][k]

n, mem, time = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

for _ in range(mem):
    x, y = map(int, input().split(" "))
    graph[x-1][y-1] = 10
x, y = map(int, input().split(" "))
graph[x-1][y-1] = -1

for i in range(1, time+1):
    move()
    if flag == -1:
        break
    length, sx, sy = getSquare()
    turn(length, sx, sy)
    
print(ans)
for i in range(n):
    for k in range(n):
        if graph[i][k] == -1:
            print(i+1, k+1)
            exit(0)