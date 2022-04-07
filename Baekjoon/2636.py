'''
'치즈'
문제 : 정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈가 놓여 있다. 판의 가장자리에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.
이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 
구멍 속으로 공기가 들어가게 된다.입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 
모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

출력 : 첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.

comment : 처음에는 치즈를 기준으로 탐색을 생각해서 답을 생각해내기가 어려웠는데, 겉에 있는 치즈를 없애야 하니까 치즈가 없는 기준으로 탐색하면 되지 않을까 생각했다.
그렇게 생각하고 나니까 문제풀기가 훨씬 수월했다.
'''
import sys
from collections import deque

a, b = map(int, input().split())
array = []
for i in range(a):
    array.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 겉에있는 치즈 체크 함수
def bfs(x, y):
    Xqueue = deque([x])
    Yqueue = deque([y])

    #처음부터 치즈가 존재할 경우
    if array[x][y] == 1:
        array[x][y] = 2
    else:
        array[x][y] = -1
        
    while Xqueue:
        x = Xqueue.popleft()
        y = Yqueue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= a or my < 0 or my >= b:
                continue
            else:
                if array[mx][my] == 1:
                    array[mx][my] = 2
                elif array[mx][my] == 0:
                    array[mx][my] = -1
                    Xqueue.append(mx)
                    Yqueue.append(my)

# 겉에있는 치즈 제거 함수
def popCheese():
    cnt = 0
    for i in range(a):
        for j in range(b):
            if array[i][j] == 2:
                array[i][j] = 0
                cnt += 1
            if array[i][j] == -1:
                array[i][j] = 0
    return cnt

result = 0
cheeseCnt = 0
while True:
    bfs(0, 0)
    temp = popCheese()
    if temp != 0:
        result += 1
        cheeseCnt = temp
    else:
        break

print(result)
print(cheeseCnt)