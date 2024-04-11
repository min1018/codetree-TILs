dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def medMove(initmed, d, far): # 특수 영양제 이동
    currMed = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if initmed[i][k] == 1:
                nx = (i + dx[d-1]*far) % n
                ny = (k + dy[d-1]*far) % n
                while nx < 0:
                    nx += n
                while ny < 0:
                    ny += n
                currMed[nx][ny] = 1
    return currMed

def grow(currmed):
    medWas = []
    tx = [-1, 1, -1, 1]
    ty = [1, -1, -1, 1]
    for i in range(n):
        for k in range(n):
            if currmed[i][k] == 1:
                medWas.append((i,k))
                graph[i][k] += 1
    #print("drink med", graph)
    for x, y in medWas:
        for h in range(4):
            nx = x + tx[h]
            ny = y + ty[h]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] >= 1:
                    graph[x][y] += 1               
    return medWas

def makeMed(medWas):
    nextMed = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if (i, k) not in medWas and graph[i][k] >= 2:
                graph[i][k] -= 2
                nextMed[i][k] = 1
    return nextMed

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
initmed = [[0] * n for _ in range(n)]
# 초기 영양제 
initmed[n-1][0] = 1
initmed[n-1][1] = 1
initmed[n-2][0] = 1
initmed[n-2][1] = 1

for _ in range(m):
    d, far = map(int, input().split())
    currmed = medMove(initmed, d, far)
    #print("after med move", currmed)
    medWas = grow(currmed)
    #print("after grow", graph)
    initmed = makeMed(medWas)
    #print("all done", graph)
    #print("next med", med)

ans = 0
for i in range(n):
    ans += sum(graph[i])
print(ans)