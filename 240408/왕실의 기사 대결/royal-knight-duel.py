from collections import deque
import time

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def moveKnight(num, dir):
    visited = [[0] * n for _ in range(n)]
    if power[num-1] - damage[num-1] <= 0:
        return
    q = deque()
    moved = [[] for _ in range(mem)]
    #print("start knight", knight)
    #print("start move", moved)

    q.append(num-1)
    while q:
        pushed = q.popleft()
        #print("pushed", pushed)
        if power[pushed] - damage[pushed] <= 0: # 이미 죽은 기사
            continue
        for k in knight[pushed]: # 산 기사
            #time.sleep(1)
            nx = k[0] + dx[dir]
            ny = k[1] + dy[dir]
            if 0 <= nx < n and 0 <= ny < n:
                # 빈칸 혹은 기사 있음
                if graph[nx][ny] != 2 and visited[nx][ny] == 0: # 벽 아님
                    moved[pushed].append([nx, ny])
                    for i in range(mem):
                        visited[nx][ny] = 1
                        #print(nx, ny, "knight[i]", knight[i])
                        if i == pushed or [nx, ny] not in knight[i]: # 빈칸
                            continue
                        else: # 기사 있음
                            q.append(i)
                            #print("append", i)
                else: # 벽이라서 못가
                     return -1
            else: # 범위 밖으로 가는 애가 하나라도 있음
                return -1
    for t in range(mem):
        if moved[t]:
            knight[t] = moved[t]
    #print("knight", knight)
    #print("moved", moved)
    for i in range(mem):
        for k in range(len(moved[i])):
            #print("i", i) # i가 1인경우
            if i != num - 1:  # 명령 받은 애는 데미지 안 받음
                x, y = moved[i][k][0], moved[i][k][1]
                if graph[x][y] == 1:  # 덫이 있고
                    damage[i] += 1

    # 명령을 받은 기사는 데미지 없음
    # 밀쳐진 기사는 도착지에 함정 잇으면 데미지



n, mem, order = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]


knight = [[] for _ in range(mem)]
power = [0 for _ in range(mem)]
damage = [0 for _ in range(mem)]
for i in range(mem):
    x, y, h, w, strength = map(int, input().split(" "))
    x, y = x-1, y-1
    power[i] = strength
    #print(x,y,h,w)
    for q in range(x, x+h):
        for h in range(y, y+w):
            #print(q, h)
            knight[i].append([q, h])



for i in range(1,order+1):
    #print("try", i)
    num, dir = map(int, input().split(" "))
    #print("original", knight)
    moveKnight(num, dir)

    #print("after",knight)
    #print("damage", damage)

ans = 0
for i in range(mem):
    if power[i] - damage[i] > 0:
        ans += damage[i]
print(ans)