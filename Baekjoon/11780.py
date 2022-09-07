'''
'플로이드 2'
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
road = [[0] * (n+1) for _ in range(n+1)]        # 효율적인 경로 리스트 (road[i][j]에 해당하는 값은 i에서 j로 가는 것보다 i에서 road[i][j]를 거쳐 j로 가는 것이 비용이 적음)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if graph[j][i]+graph[i][k] < graph[j][k]:
                road[j][k] = i
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

def solution(x, y):                             # 경로 탐색 함수
    answer = [x, y]
    end = 0
    while True:                                 # 다른 효율적인 경로를 발견하지 않을 때까지 answer 탐색
        end = 1
        for i in range(len(answer)-1):
            temp = road[answer[i]][answer[i+1]]
            if temp != 0:                       # 다른 지역을 거쳐 가는 것이 더 효율적일 경우 answer에 지역 추가
                answer.insert(i+1, temp)
                end = 0
        if end == 1:
            break
    return answer

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()


for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or graph[i][j] == INF:
            print(0)
        else:
            result = solution(i, j)
            print(len(result), *result)