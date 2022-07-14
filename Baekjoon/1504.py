'''
특정한 최단 경로
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for i in range(N+1)]


for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def d(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF for i in range(N+1)]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

d1 = d(1)           # 1이 시작점일 때의 최단경로 리스트
d2 = d(v1)          # v1이 시작점일 때의 최단경로 리스트
d3 = d(v2)          # v2이 시작점일 때의 최단경로 리스트
result = min(d1[v1]+d2[v2]+d3[N], d1[v2]+d3[v1]+d2[N])      # 1->v1->v2->N 또는 1->v2->v1->N 두가지 경로가 존재하므로 그 중 더 작은 것 저장
if result >= INF:
    print(-1)
else:
    print(result)
