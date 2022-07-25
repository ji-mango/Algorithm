'''
'키 순서'

풀이 : 1. 플로이드 워셜 알고리즘을 이용해 학생들 간의 그래프를 연결한다.
      2. 학생들 간의 연결된 그래프를 탐색하면서 자신을 지나는 학생이 n명이 맞는지 확인한다.
'''
INF = int(1e9)

n, m = map(int, input().split())
height = [[INF for i in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            height[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    height[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            height[j][k] = min(height[j][k], height[j][i]+height[i][k])

result = [0 for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if height[i][j] != INF:
            result[i] += 1
            if i != j:
                result[j] += 1

answer = 0
for i in range(1, n+1):
    if result[i] == n:
        answer += 1

print(answer)