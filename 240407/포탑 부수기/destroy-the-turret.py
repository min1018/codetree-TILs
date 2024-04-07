from collections import deque

def attackChoose():
    bomb = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                bomb.append((x, y, graph[x][y], recent[x][y]))
    bomb.sort(key=lambda x: (x[2], -x[3], -x[0] + x[1], -x[1]))
    #print("choose attacker", bomb)
    attacked, attacker = bomb[-1], bomb[0]
    graph[attacker[0]][attacker[1]] += (n+m)
    #bomb.sort(key=lambda x: (-x[2], x[3], x[0] + x[1], x[1]))
    return attacker, attacked

def layserAttack(attacker, attacked):
    ax, ay, power, turn = attacker
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((ax, ay))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    path = []
    while q:
        x, y = q.popleft()
        if x == attacked[0] and y == attacked[1]:
            graph[x][y] -= (power+n+m)
            x, y = visited[x][y]
            while True:
                if x == ax and y == ay: break
                path.append((x, y))
                graph[x][y] -= (power + n + m) // 2
                x, y = visited[x][y]
            return path
        for i in range(4):
            nx = (x + dx[i]) % n
            ny = (y + dy[i]) % m
            while nx < 0:
                nx += n
            while ny < 0:
                ny += m
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = (x, y)
    return path

def bombAttack(attacker, attacked):
    tx, ty, _, _ = attacked
    path = []
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]
    for i in range(8):
        nx = (tx + dx[i]) % n
        ny = (ty + dy[i]) % m
        while nx < 0 :
            nx += n
        while ny < 0:
            ny += m
        if 0 <= nx < n and 0 <= ny < m and nx != tx and ny != ty:
            if graph[nx][ny] != 0:
                graph[nx][ny] -= (attacker[2]+n+m)//2
                path.append((nx, ny))
    graph[attacked[0]][attacked[1]] -= (attacker[2]+n+m)
    #print("after bomb in func ",graph)
    #print("bomb path", path)
    return path


def reset(path):
    for i in range(n):
        for k in range(m):
            if (i, k) not in path and (i, k) != (attacked[0], attacked[1]) and (i, k) != (attacker[0], attacker[1]) and graph[i][k] != 0:
                graph[i][k] += 1
            if graph[i][k] < 0:
                graph[i][k] = 0



n, m, k = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
recent = [[0] * m for _ in range(n)]

for i in range(1, k+1):
    #print("try ", i)
    attacker, attacked = attackChoose()
    recent[attacker[0]][attacker[1]] = i
    #print(attacker, attacked)
    path = layserAttack(attacker, attacked)

    if len(path) == 0:
        path = bombAttack(attacker, attacked)
        # print("path", path)
        # print("after bomb")
    #else:
        # print("path", path)
        # print("after layser")
    reset(path)



ans = 0
#print(graph)
for x in range(n):
    ans = max(ans, max(graph[x]))
print(ans)