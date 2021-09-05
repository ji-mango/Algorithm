'''
'게임 개발'
문제 : 현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다. 캐릭터가 있는 장소는
      N X M 크기의 직사각형으로, 각 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다.
      맵의 각 칸은 (A,B)로 나타낼 수 있고, A는 북쪽으로부터, B는 서쪽으로부터 떨어진 칸의 개수이다.
      캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다. 캐릭터가 움직이는 매뉴얼은 이러하다.

      1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도)부터 차례대로 갈 곳을 정한다.
      2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진한다.
         왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
      3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우, 바라보는 방향을 유지한 채로 한칸 뒤로 가고
         1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

      매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

comment :
'''
n, m = map(int, (input().split()))      # 세로n, 가로m 맵 생성
a, b, d = map(int, (input().split()))   # (a,b)에 d쪽을 바라보고 서 있는 캐릭터(d가 0: 북쪽, 1: 동쪽, 2:남쪽, 3:서쪽)
board = [input().split() for row in range(n)]   # 맵 생성 (0:육지, 1:바다)
for i in range(n):
    for j in range(m):
        board[i][j] = int(board[i][j])

# 방향(d)에 따른 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board[a][b] = 2
count = 1

while True:
    #  네 방향 모두 가본 칸이거나 바다로 되어 있는 칸인 경우
    if board[a+dx[0]][b+dy[0]] != 0 and board[a+dx[1]][b+dy[1]] != 0 and board[a+dx[2]][b+dy[2]] != 0 and board[a+dx[3]][b+dy[3]] != 0:
        if d == 0 or d == 1:
            tempD = d+2
        else:
            tempD = d-2

        if board[a+dx[tempD]][b+dy[tempD]] == 1:    # 뒤쪽 방향이 바다인 칸일 경우 while문 빠져나옴
            break
        else:                                       # 아닐 경우 뒤로 한 칸 이동
            a = a+dx[tempD]
            b = b+dy[tempD]
        continue

    # 왼쪽 방향으로 회전
    if d == 0:
        d = 3
    else:
        d = d-1

    # 회전한 후 정면에 가본 곳이 아닐 경우 이동
    tempA = a + dx[d]
    tempB = b + dy[d]
    if board[tempA][tempB] == 0:
        a = tempA
        b = tempB
        board[a][b] = 2
        count += 1

print(count)