'''
'연구소 3'
'''
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
virusList = []
wallList = []
board = []

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 2:
            virusList.append([i, j])
            board[i][j] = '*'            
        elif board[i][j] == 1:
            wallList.append([i, j])
            board[i][j] = '-'            
        elif board[i][j] == 0:
            board[i][j] = -2                # -2이면 빈칸

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 99999999
end = n*n

def dfs(comb, depth):                       # 조합을 dfs함수로 구현
    global result, end, n, m
    if len(comb) == m:
        virus(comb)
        return
    elif depth == len(virusList):
        return
    
    comb.append(virusList[depth])
    dfs(comb, depth + 1)

    comb.pop()
    dfs(comb, depth + 1)

def virus(comb):                            # 바이러스 활성 과정
    global result, end, n, m
    cnt = len(wallList) + len(virusList)    
    compare = cnt
    second = 0
    new_board = deepcopy(board)
    queue = deque()

    for i in comb:
        new_board[i[0]][i[1]] = second
        queue.append([i[0], i[1]])

    while True:
        if cnt == end:                      # (벽 개수 + 원래 바이러스 개수 + 바이러스 되는 것의 개수) == (칸의 총 개수) 이면 종료 
            if second < result:             # 최소 시간 갱신
                result = second
            break
        second += 1                         # 초
        length = len(queue)
        for i in range(length):
            x, y = queue.popleft()
            for i in range(4):              # 상하좌우 바이러스 활성화
                mx = x + dx[i]
                my = y + dy[i]
                if mx < 0 or mx >= n or my < 0 or my >= n:
                    continue
                elif new_board[mx][my] == '-':
                    continue
                elif new_board[mx][my] == -2 or new_board[mx][my] == '*':
                    if new_board[mx][my] == -2:         # 빈칸이었는데 활성 바이러스 되는 경우 cnt++
                        cnt += 1                        
                    if new_board[mx][my] == '*':        # 비활성 바이러스인 경우      
                        compare -= 1                    # 주위에 *(비활성화 바이러스)밖에 없는 경우에 break하지 않기 위해 compare값 변경
                    queue.append([mx, my])
                    new_board[mx][my] = second    
        if cnt == compare:                              # 이전 cnt와 바이러스 활성화 후 cnt가 같을 경우 더이상 바이러스가 옮길 수 없는 상태이므로 종료
            break
        else:
            compare = cnt

dfs(deque(), 0)
if result == 99999999:
    print(-1)
else:
    print(result)