from collections import deque
import time

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

flag = 0

def moveKnight(num, dir):
    global flag
    if power[num-1] - damage[num-1] == 0:
        flag = -1
        return -1
    q = deque()
    moved = [[] for _ in range(n)]
    q.append(num-1)
    while q:
        pushed = q.popleft()
        #print("pushed", pushed)
        if power[pushed] - damage[pushed] == 0: # 이미 죽은 기사
            continue
        for k in knight[pushed]: # 산 기사
            #time.sleep(1)
            nx = k[0] + dx[dir]
            ny = k[1] + dy[dir]
            if 0 <= nx < n and 0 <= ny < n:
                # 빈칸 혹은 기사 있음
                if graph[nx][ny] != 2: # 벽 아님
                    moved[pushed].append([nx, ny])
                    for i in range(n): # 빈칸
                        #print(nx, ny, "knight[i]", knight[i])
                        if i == pushed or [nx, ny] not in knight[i]:
                            continue
                        else: # 기사 있음
                            q.append(i)
                            #print("append", i)
                else:
                     return -1
            else: # 범위 밖으로 가는 애가 하나라도 있음
                return -1
    for t in range(n):
        if moved[t]:
            knight[t] = moved[t]
    #print("moved", moved)
    for i in range(n):
        for k in range(len(moved[i])):
            #print("i", i) # i가 1인경우
            if i != num - 1:  # 명령 받은 애는 데미지 안 받음
                x, y = moved[i][k][0], moved[i][k][1]
                if graph[x][y] == 1:  # 덫이 있고
                    #print(x, y)
                    if damage[i] > power[i]:
                        #print("in if")
                        continue
                    else:
                        #print("in else")
                        damage[i] += 1

    # 명령을 받은 기사는 데미지 없음
    # 밀쳐진 기사는 도착지에 함정 잇으면 데미지


# def calcDamage(num, moved):
#     for i in range(n):
#         for k in range(len(moved[i])):
#             if i != num-1: # 명령 받은 애는 데미지 안 받음
#                 x, y = moved[i][k][0], moved[i][k][1]
#                 if graph[x][y] == 1: # 덫이 있고
#                     if damage[i] > power[i]:
#                         continue
#                     else:
#                         damage[i] += 1




n, mem, order = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]


knight = [[] for _ in range(n)]
power = [0 for _ in range(n)]
damage = [0 for _ in range(n)]
for i in range(1, mem+1):
    x, y, h, w, strength = map(int, input().split(" "))
    x, y = x-1, y-1
    power[i-1] = strength
    #print(x,y,h,w)
    for q in range(x, x+h):
        for h in range(y, y+w):
            #print(q, h)
            knight[i-1].append([q, h])



for i in range(1,order+1):
    #print("try", i)
    num, dir = map(int, input().split(" "))
    #print("original", knight)
    t = moveKnight(num, dir)
    #print("after",knight)

    #print("damage", damage)
    # if t == -1:
    #     continue
    # else:
    #     calcDamage()

ans = 0
for i in range(n):
    if power[i] - damage[i] != 0:
        ans += damage[i]
print(ans)

# def gravity():
#     n = len(arr)
#     m = len(arr[0])
#     for i in range(n-1):
#         for k in range(m):
#             p = i
#             while 0 <= p and arr[p][j] == 1 and arr[p+1][j] == 0:
#                 arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j]
#                 p -= 1