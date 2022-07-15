'''
'감시'

comment : 다시 풀어야함
'''
from copy import deepcopy

N, M = map(int, input().split())
board = []
cctv = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        if board[i][j] in [1,2,3,4,5]:
            cctv.append([board[i][j], i, j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0,3]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

def fill(array, n, x, y):
    for i in n:                 # 각 방향에 대해 움직이기 위한 반복문
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if array[nx][ny] == 6:
                break
            if array[nx][ny] == 0:
                array[nx][ny] = '#'

def dfs(depth, arr):
    global minimum
    if depth == len(cctv):
        count = 0
        for i in range(N):
            count += arr[i].count(0)
        minimum = min(minimum, count)
        return
    
    temp = deepcopy(arr)
    cctv_mode, x, y = cctv[depth]
    for i in mode[cctv_mode]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = deepcopy(arr)
        
minimum = int(1e9)
dfs(0, board)
print(minimum)