'''
'연구소'
문제 : 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는
아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로
나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다. 벽을 3개 세운 뒤, 바이러스가
퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.
2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다. 빈 칸의 개수는 3개 이상이다.

출력 : 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

comment : 백준에서 골드문제는 이 문제가 처음이라 어려웠는데, 그래도 풀고나니까 많이 뿌듯했다.
이 문제는 combinations를 사용하는 것이 핵심인 것 같다.
'''
from itertools import combinations
import copy

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max = 0

def dfs(x, y):
    temp[x][y] = 3
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or my < 0 or mx >= N or my >= M:
            continue
        elif temp[mx][my] == 0:
            dfs(mx, my)
array = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            array.append((i,j))

for i in combinations(array, 3):
    temp = copy.deepcopy(graph)
    temp[i[0][0]][i[0][1]] = 1
    temp[i[1][0]][i[1][1]] = 1
    temp[i[2][0]][i[2][1]] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                dfs(i, j)
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1
    if max < count:
        max = count

print(max)