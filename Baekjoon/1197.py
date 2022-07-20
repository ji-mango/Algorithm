'''
'최소 스패닝 트리'
'''
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = []
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort()

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
for i in graph:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        result += i[0]
        union_parent(parent, i[1], i[2])

print(result)