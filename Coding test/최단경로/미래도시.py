'''
'미래도시'
'''
# 다익스트라 알고리즘
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


