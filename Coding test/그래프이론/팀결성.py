import sys
input = sys.stdin.readline

N, M = map(int, input().split())

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

parent = [0 for i in range(N+1)]
for i in range(N+1):
    parent[i] = i

for i in range(M):
    x, y, z = map(int, input().split())
    if x == 0:
        union_parent(parent, y, z)
    else:
        if find_parent(parent, y) == find_parent(parent, z):
            print("YES")
        else:
            print("NO")

print(parent)
