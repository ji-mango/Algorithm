'''
'도시 분할 계획'
'''
import sys
input = sys.stdin.readline
graph = []

N, M = map(int, input().split())
for i in range(M):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
max_value = 0
for i in graph:
    cost, a, b = i
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    union_parent(parent, a, b)
    result += cost
    max_value = cost

print(result - max_value)