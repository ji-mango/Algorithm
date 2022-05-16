'''
'빗물'
문제 : 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

입력 : 첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.
따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

출력 : 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
빗물이 전혀 고이지 않을 경우 0을 출력하여라.

'''
hw = map(int, input().split())
array = list(map(int, input().split()))
board = [[0 fo, r i in range(w)] for i in range(max(array))]

for i in range(max(array)):
    for j in range(w):
        if i <= array[j]-1:
            board[i][j] = 1

def solv(x, y):
    global w
    global cnt
    y += 1
    while True:
        if y >= w:
            return False
        if board[x][y] == 1:
            return True
        if board[x][y] == 0:
            cnt += 1
        y = y+1

result = 0
for i in range(max(array)):
    for j in range(w):
        cnt = 0
        if board[i][j] == 1:
            if solv(i,j):
                result += cnt
        j += cnt

print(result)