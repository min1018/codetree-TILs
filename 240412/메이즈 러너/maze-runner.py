def playerMove():
    global move
    global done
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(player)):
        poss = []
        if len(player[i]) > 0:
            x, y = player[i][0], player[i][1]
            currDist = abs(ex-x)+abs(ey-y)
            for h in range(4):
                nx = x + dx[h]
                ny = y + dy[h]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                    moveDist = abs(ex-nx)+abs(ey-ny)
                    #print("nx, ny, currDist, moveDist", nx, ny, currDist, moveDist)
                    if moveDist < currDist:
                        poss.append((moveDist, nx, ny))
            #print(i, poss)
            if len(poss) > 0:
                move += 1
                poss.sort(key= lambda x : (x[0]))
                if poss[0][0] == 0:
                    player[i] = []
                    done += 1
                else:
                    player[i] = [poss[0][1], poss[0][2]]

def searchSqaure():
    poss = []
    for i in range(n):
        for k in range(n):
            if (i, k) != (ex, ey):
                length = max(abs(i - ex), abs(k - ey))+1
                if i > ex: 
                    lx, sx = i, ex
                else: 
                    lx, sx = ex, i
                if k > ey: 
                    ly, sy = k, ey
                else: 
                    ly, sy = ey, k

                flag = 0
                #사각형안에 선수 있는가 
                for h in range(len(player)):
                    if len(player[h]) > 0:
                        x, y = player[h]
                        if sx <= x <= lx and sy <= y <= ly:
                            flag = 1
                            break
                if flag == 1:
                    poss.append((length, sx, sy))
    poss.sort(key = lambda x: (x[0], x[1], x[2]))
    return poss[0][0], poss[0][1], poss[0][2]
                

def rotateSqaure(length, sx, sy):
    new = [[0] * n for _ in range(n)]
    for x in range(sx, sx+length):
        for y in range(sy, sy+length):
            ox, oy = x-sx, y-sy
            mx, my = oy, length - 1 - ox
            new[sx + mx][sy + my] = graph[x][y]
     #print("new", new)
    for i in range(sx, sx+length):
        for k in range(sy, sy+length):
            if new[i][k] != 0:
                graph[i][k] = new[i][k] - 1
            else:
                graph[i][k] = new[i][k]

def playerExitRotate(length, sx, sy):
    global ex, ey
    #player
    for i in range(len(player)):
        if len(player[i]) > 0:
            x, y = player[i]
            if sx <= x < sx+length and sy <= y < sy+length:
                ox, oy = x-sx, y-sy
                mx, my = oy, length-1-ox
                player[i] = [sx+mx, sy+my]
    #exit
    if sx <= ex < sx+length and sy <= ey < sy+length:
        ox, oy = ex-sx, ey-sy
        mx, my = oy, length-1-ox
        ex, ey = sx+mx, sy+my
    



n, mem, k= map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
player = []
move = 0
done = 0
for _ in range(mem):
    x, y = map(int, input().split())
    player.append([x-1, y-1])
ex, ey = map(int, input().split())
ex, ey = ex-1, ey-1


for T in range(k):
    # print(T+1)
    # 모든 참가자 탈출 시 종료 
    #print(player)
    playerMove()
    if done == mem:
        break
    #print(player)
    length, sx, sy = searchSqaure()
    #print("square", length, sx, sy)
    rotateSqaure(length, sx, sy)
    playerExitRotate(length, sx, sy)
    # print(graph)
    # print("player", player)
    # print("exit", ex, ey)
    # print("move", move)

# 이동거리 합, 출구 좌표 
print(move)
print(ex+1, ey+1)