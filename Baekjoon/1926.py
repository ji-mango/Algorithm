'''
'그림'
문제 : 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의
넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은
 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

comment : dfs로 풀면 방문하지 않는 부분이 생겨 bfs로 풀었다.
'''
from collections import deque
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global x, y
    global width
    queueX = deque([x])
    queueY = deque([y])
    board[x][y] = 2
    while queueX:
        x = queueX.popleft()
        y = queueY.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue
            elif board[mx][my] == 1:
                width += 1
                board[mx][my] = 2
                queueX.append(mx)
                queueY.append(my)



count = 0
max = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            x = i
            y = j
            count += 1
            width = 1
            bfs()
            if max < width:
                max = width
print(count)
print(max)

