'''
'네트워크 연결'
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

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

edges = []
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

for i in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    edges.append((c, a, b))

edges.sort()

result = 0
for i in edges:
    c, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        result += c
        union_parent(parent, a, b)

print(result)
