dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def playerMove(cx, cy, d):
    nx = cx + dx[d]
    ny = cy + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        return nx, ny, d
    elif d in [0,2]:
        if d == 0 :
            d = 2
        elif d == 2:
            d = 0
        nx, ny = cx + dx[d], cy + dy[d]
    elif d in [1,3]:
        if d == 1 :
            d = 3
        elif d == 3:
            d = 1
        nx, ny = cx + dx[d], cy + dy[d]
    return nx, ny, d


def play(px, py, d, power, gun, i):
    flag = 0
    for num in range(len(player)):
        # 1. 다른 플레이어 만남
        if num != i and px == player[num][0] and py == player[num][1]: 
            flag = 1
            p1 = power + gun
            p2 = player[num][3]+player[num][4]
            win = 0
            # 포인트 획득 및 진사람 땅에 총 놓기
            if p1 > p2 : # i가 이김 
                point[i] += abs(p1- p2)
                win, loose = i, num
                graph[px][py].append(player[num][4])
            elif p1 < p2: # num 이 이김 
                point[num] += abs(p1- p2)
                win, loose = num, i
                graph[px][py].append(player[i][4])
            elif p1 == p2: 
                if power > player[num][3]:
                    point[i] += abs(p1- p2)
                    win, loose = i, num
                    graph[px][py].append(player[num][4])
                else:
                    point[num] += abs(p1- p2)
                    win, loose = num, i
                    graph[px][py].append(player[i][4])

            # 이긴 사람 총 교체 
            for t in range(len(graph[px][py])):
                if player[win][4] < graph[px][py][t]:
                    player[win][4], graph[px][py][t] = player[win][4], graph[px][py][t]

            # player 진 -> 간 땅에 초이 있으면 줍, 없으면 gun 0
            while True:
                nx = player[loose][0] + dx[player[loose][2]]
                ny = player[loose][1] + dy[player[loose][2]]
                sign = 0
                if 0 <= nx < n and 0 <= ny < n:
                    for p in range(len(player)):
                        if nx == player[p][0] and ny == player[p][1]:
                            sign = 1 #사람 있음 
                    if sign == 1:
                        player[loose][2] = (player[loose][2] + 5)%4 # 사람이 있는 경우 회전 
                    
                else: # 범위 밖
                    sign = 1
                    player[loose][2] = (player[loose][2] + 5)%4 # 벽이 있는 경우 회전 
                    
                # 사람 있으면 혹은 벽이라면 -> 90도 회전 
                if sign == 0:
                    player[loose][0], player[loose][1] = nx, ny
                    if len(graph[nx][ny]) > 0:
                        for tg in range(len(graph[nx][ny])):
                            if graph[nx][ny][tg] > 0:
                                player[loose][4], graph[nx][ny][tg] = graph[nx][ny][tg], player[loose][4]
                    break


    if flag == 0: 
        if len(graph[px][py]) > 0: # 2. 총 있음 
            for g in range(len(graph[px][py])):
                if graph[px][py][g] > gun :# 더 큰 총이 있으면 
                    graph[px][py][g], player[i][4] = player[i][4], graph[px][py][g] # 바꿔치기

        else: # 그냥 빈칸 
            player[i] = [px, py, d, power, gun]

    




n, mem, game = map(int, input().split())
graph = [[] for _ in range(n)]
point = [0 for _ in range(mem)]
for a in range(n):
    temp = list(map(int, input().split()))
    for b in temp:
        graph[a].append([b])
player = []

for a in range(mem):
    x, y, d, power = map(int, input().split())
    player.append([x-1, y-1, d, power, 0]) # 마지막 총 


for _ in range(game):
    for i in range(mem):
        # print("player", i, player[i])
        cx, cy, d, power, gun = player[i]
        nx, ny, d = playerMove(cx, cy, d)
        player[i] = [nx, ny, d, power, gun]
        play(nx, ny, d, power, gun, i)
        # print("graph", graph)
        # print("player", player)
    
print(*point)