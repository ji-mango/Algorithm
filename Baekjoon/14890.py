'''
'경사로'

comment : 다양한 경우의 수가 존재해서 그걸 생각하는 것이 조금 까다로운 문제였다.
'''
n, l = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def checkX(x):                  # 가로 방향 길 체크 함수
    global n, l
    cnt = 1
    step = board[x][0]
    isTop = 1                           # 양 옆 길보다 높은 길일 경우를 구분하기 위한 변수
    load = 0                            # 경사로를 깔은 길일 경우를 구분하기 위한 변수(경사로는 겹쳐 놓을 수 없으므로)
    for i in range(1, n):
        if board[x][i] == step:         # 앞의 길과 현재 길의 높이가 같을 때
            cnt += 1
        elif board[x][i] == step-1:     # 앞의 길보다 현재 길의 높이가 한 칸 더 낮을 때
            if isTop == 1:
                isTop = 0
                cnt = 1
                step -= 1
                load = 1
            elif cnt >= l:
                cnt = 1
                step -= 1
                load = 1
            else:
                return False
        elif board[x][i] == step+1:     # 앞의 길보다 현재 길의 높이가 한 칸 더 높을 때
            if cnt >= l:
                if load == 1:           # 경사로가 놓여져 있을 경우
                    if cnt < 2*l:       # 하나 더 놓을 수 있는 거리인지 확인
                        return False
                isTop = 1
                cnt = 1
                step += 1
                load = 0
            else:
                return False
        else:                           # 그 외의 경우
            return False
    if isTop == 1 or cnt >= l:
        return True
    else:
        return False

def checkY(y):                  # 세로 방향 길 체크 함수
    global n, l
    cnt = 1
    step = board[0][y]
    isTop = 1
    load = 0
    for i in range(1, n):
        if board[i][y] == step:
            cnt += 1
        elif board[i][y] == step-1:
            if isTop == 1:
                isTop = 0
                cnt = 1
                step -= 1
                load = 1
            elif cnt >= l:
                cnt = 1
                step -= 1
                load = 1
            else:
                return False
        elif board[i][y] == step+1:
            if cnt >= l:
                if load == 1:
                    if cnt < 2*l:
                        return False
                isTop = 1
                cnt = 1
                step += 1
                load = 0
            else:
                return False
        else:
            return False
    if isTop == 1 or cnt >= l:
        return True
    else:
        return False

answer = 0
for i in range(n):
    result = checkX(i)
    if result:
        answer += 1
    result = checkY(i)
    if result:
        answer += 1

print(answer)