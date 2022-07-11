'''
'최단경로'
'''
# 플로이드 워셜 알고리즘 - 메모리 초과
'''
import sys

INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF for _ in range(v+1)] for i in range(v+1)]

for i in range(1, v+1):
    for j in range(1, v+1):
        if i==j:
            graph[i][j] = 0

start = int(input())

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

for i in range(1, v+1):
    if graph[start][i] >= INF:
        print("INF")
    else:
        print(graph[start][i]) 
'''
# 다익스트라 알고리즘
import heapq
import sys
INF = int(1e9)

V, E = map(int, input().split())
graph = [[]for i in range(V+1)]
distance = [INF for i in range(V+1)]

K = int(input())
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def d(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

d(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])