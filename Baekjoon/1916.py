'''
'최소비용 구하기'

comment : 처음에 graph에 버스 비용을 모두 넣어서 느렸는데, 
graph를 dictionary 자료형으로 초기화해서 출발점과 도착점이 같은 버스 중 최소 비용만 넣고, end값일 때 함수를 멈춰서 더 빨랐다.
그리고 sys.stdin.readline을 사용하지 않아서 시간초과가 떴는데 사용하니까 시간초과가 뜨지 않았다.
sys.stdin.readline()가 내 생각보다 훨씬 빠른 함수라는 것을 깨달았다.
'''
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())
graph = [{} for i in range(n+1)]
distance = [INF for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

start, end = map(int, input().split())

def d(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        elif now == end:
            break
        for key, value in graph[now].items():
            cost = dist + value
            if cost < distance[key]:
                distance[key] = cost
                heapq.heappush(q, (cost, key))

d(start, end)
print(distance[end])