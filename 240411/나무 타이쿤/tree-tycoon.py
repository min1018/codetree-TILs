dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def medMove(med, d, far):
    newMed = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if med[i][k] == 1:
                nx = (i + dx[d-1]*far) % n
                ny = (k + dy[d-1]*far) % n
                while nx < 0:
                    nx += n
                while ny < 0:
                    ny += n
                if 0 <= nx < n and 0 <= ny < n:
                    newMed[nx][ny] = 1
    return newMed

def grow(med):
    tx = [-1, 1, -1, 1]
    ty = [1, -1, -1, 1]
    for i in range(n):
        for k in range(n):
            if med[i][k] == 1:
                graph[i][k] += 1
    for a in range(n):
        for b in range(n):
            if med[a][b] == 1:
                for h in range(4):
                    nx = a + tx[h]
                    ny = b + ty[h]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] >= 1:
                            graph[a][b] += 1

def makeMed(med):
    for i in range(n):
        for k in range(n):
            if graph[i][k] >= 2 and med[i][k] != 1:
                graph[i][k] -= 2
                med[i][k] = 1
            elif med[i][k] == 1:
                med[i][k] = 0
    return med

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
med = [[0] * n for _ in range(n)]
med[n-1][0] = 1
med[n-1][1] = 1
med[n-2][0] = 1
med[n-2][1] = 1
d, far = map(int, input().split())

for _ in range(m):
    currmed = medMove(med, d, far)
    grow(currmed)
    med = makeMed(currmed)

ans = 0
for i in range(n):
    ans += sum(graph[i])
print(ans)