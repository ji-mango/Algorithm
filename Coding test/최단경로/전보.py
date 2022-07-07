'''
'전보'
'''

import heapq

n, m, c = map(int, input().split())
road = [[] for i in range(n+1)]
for i in range(m):
    x, y, z = map(int, input().split())
    road[x].append((y, z))

distance = [9999999 for i in range(n+1)]
def d(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in road[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

d(c)

total_cnt = 0
total_time = 0
for i in range(1, n+1):
    if distance[i] == 9999999:
        continue
    elif i == c:
        continue
    else:
        total_cnt += 1
        if total_time < distance[i]:
            total_time = distance[i]

print(distance)
print(total_cnt, total_time)