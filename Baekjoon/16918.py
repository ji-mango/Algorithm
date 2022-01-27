'''
'봄버맨'
문제 : 봄버맨은 크기가 R×C인 직사각형 격자판 위에서 살고 있다. 격자의 각 칸은 비어있거나 폭탄이 들어있다.

폭탄이 있는 칸은 3초가 지난 후에 폭발하고, 폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸이 되며,
인접한 네 칸도 함께 파괴된다. 즉, 폭탄이 있던 칸이 (i, j)인 경우에 (i+1, j), (i-1, j), (i, j+1), (i, j-1)도
함께 파괴된다. 만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다.
따라서, 연쇄 반응은 없다.

봄버맨은 폭탄에 면역력을 가지고 있어서, 격자판의 모든 칸을 자유롭게 이동할 수 있다. 봄버맨은 다음과 같이 행동한다.

가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
다음 1초 동안 봄버맨은 아무것도 하지 않는다.
다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
3과 4를 반복한다.
폭탄을 설치해놓은 초기 상태가 주어졌을 때, N초가 흐른 후의 격자판 상태를 구하려고 한다.

comment : N이 1(초기상태)일 때는 초기상태 그대로, N이 짝수일 때는 모든 칸에 폭탄이 존재하도록,
N을 4로 나눴을 때 나머지가 3일 경우는 처음에 놨던 폭탄이 터지는 경우로, N을 4로 나눴을 때 나머지가 1일 경우
처음에 놨던 폭탄 다음에 놓아둔 폭탄이 터지는 경우로 나누어 출력했다.
'''
from collections import deque

R, C, N = map(int, input().split())
board = []
for i in range(R):
    board.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    board[i] = list(board[i])


def solution():
    temp_board = []
    for i in range(R):
        temp_board.append('O'*C)
    for i in range(R):
        temp_board[i] = list(temp_board[i])
    queue_x = deque()
    queue_y = deque()
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                queue_x.append(i)
                queue_y.append(j)
                temp_board[i][j] = '.'
    while(queue_x):
        x = queue_x.popleft()
        y = queue_y.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= R or my < 0 or my >= C:
                continue
            else:
                temp_board[mx][my] = '.'
    return temp_board


if N % 2 == 0:
    board = [list('O'*C)]*R
    result = ''
    for i in range(R):
        for j in range(C):
            result += board[i][j]
        print(result)
        result = ''
elif N == 1:
    result = ''
    for i in range(R):
        for j in range(C):
            result += board[i][j]
        print(result)
        result = ''
elif N % 4 == 3:
    result = ''
    board = solution()
    for i in range(R):
        for j in range(C):
            result += board[i][j]
        print(result)
        result = ''
elif N % 4 == 1:
    result = ''
    board = solution()
    board = solution()
    for i in range(R):
        for j in range(C):
            result += board[i][j]
        print(result)
        result = ''

