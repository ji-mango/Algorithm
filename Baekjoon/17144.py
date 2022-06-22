'''
'미세먼지 안녕!'
'''
r, c, t = map(int, input().split())
board = []
clean = []
for i in range(r):
    board.append(list(map(int, input().split())))
    for j in range(c):
        if board[i][j] == -1:
            clean.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def diffusion(r, c, board):                                     # 먼지 확산 함수
    new_board = [[0 for i in range(c)] for i in range(r)]
    new_board[clean[0][0]][clean[0][1]] = -1
    new_board[clean[1][0]][clean[1][1]] = -1
    for i in range(r):
        for j in range(c):
            dust = board[i][j]
            if dust != -1 and dust != 0:
                cnt = 0     # 확산된 방향의 개수
                for k in range(4):
                    mx = i + dx[k]
                    my = j + dy[k]
                    if mx < 0 or mx >= r or my < 0 or my >= c:
                        continue
                    if board[mx][my] == -1:
                        new_board[mx][my] == -1
                    else:
                        new_board[mx][my] += dust//5
                        cnt += 1
                new_board[i][j] += dust - ((dust//5)*cnt)
    return new_board

def wind(r, c, clean, board):                                   # 공기청정기 바람
    x1, y1 = clean[0][0], clean[0][1]
    x2, y2 = clean[1][0], clean[1][1]

    temp1 = 0   # 위쪽 청정기 방향 세는 변수
    temp2 = 0   # 아래쪽 청정기 방향 세는 변수
    y1 += 1
    y2 += 1
    dust1, board[x1][y1] = board[x1][y1], 0
    dust2, board[x2][y2] = board[x2][y2], 0
    while True:
        if temp1 == 0:
            y1 += 1
            if y1 >= c:
                y1 -= 1
                temp1 += 1
        
        if temp1 == 1:
            x1 -= 1
            if x1 < 0:
                x1 += 1
                temp1 += 1
        if temp1 == 2:
            y1 -= 1
            if y1 < 0:
                y1 += 1
                temp1 += 1
        if temp1 == 3:
            x1 += 1
            if x1 == clean[0][0] and y1 == clean[0][1]:
                temp1 += 1

        if temp2 == 0:
            y2 += 1
            if y2 >= c:
                y2 -= 1
                temp2 += 1
        if temp2 == 1:
            x2 += 1
            if x2 >= r:
                x2 -= 1
                temp2 += 1
        if temp2 == 2:
            y2 -= 1
            if y2 < 0:
                y2 += 1
                temp2 += 1
        if temp2 == 3:
            x2 -= 1
            if x2 == clean[1][0] and y2 == clean[1][1]:
                temp2 += 1

        if temp1 == 4 and temp2 == 4:
            break

        dust1, board[x1][y1] = board[x1][y1], dust1
        dust2, board[x2][y2] = board[x2][y2], dust2

    return board

for i in range(t):
    board = diffusion(r,c,board)
    board = wind(r, c, clean, board)

result = 0
for i in range(r):
    result += sum(board[i])

print(result+2)