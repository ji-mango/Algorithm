'''
'미래도시'
'''
# 다익스트라 알고리즘
'''
import heapq

n, m = map(int, input().split())
company = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    company[a].append(b)
    company[b].append(a)

x, k = map(int, input().split())

def sol(start):
    distance = [999999 for i in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in company[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    return distance

result = 0
distance = sol(1)
if distance[k] == 999999:
    result = -1
else:
    result += distance[k]
    distance = sol(k)
    if distance[x] == 999999:
        result = -1
    else:
        result += distance[x]

print(result)
'''

# 플로이드 워셜 알고리즘
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF for i in range(n+1)] for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

result = graph[1][k] + graph[k][x]
if result >= INF:
    result = -1
print(result)

for i in range(n+1):
    print(graph[i])

