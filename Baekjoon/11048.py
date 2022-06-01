'''
'이동하기'
문제 : 준규는 N×M 크기의 미로에 갇혀있다. 미로는 1×1크기의 방으로 나누어져 있고, 각 방에는 사탕이 놓여져 있다. 미로의 가장 왼쪽 윗 방은 (1, 1)이고, 
가장 오른쪽 아랫 방은 (N, M)이다. 준규는 현재 (1, 1)에 있고, (N, M)으로 이동하려고 한다. 준규가 (r, c)에 있으면, 
(r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있고, 각 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다. 
또, 미로 밖으로 나갈 수는 없다. 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.

입력 : 첫째 줄에 미로의 크기 N, M이 주어진다. (1 ≤ N, M ≤ 1,000)
둘째 줄부터 N개 줄에는 총 M개의 숫자가 주어지며, r번째 줄의 c번째 수는 (r, c)에 놓여져 있는 사탕의 개수이다. 
사탕의 개수는 0보다 크거나 같고, 100보다 작거나 같다.

출력 : 첫째 줄에 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수를 출력한다.

풀이 : (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있으므로 위쪽 방향, 대각선 위방향, 왼쪽 방향에서 가장 큰 값에 현재 값을 더하면서 풀었다.

comment : 한눈에 딱 보이는 점화식이라서 쉽게 풀 수 있었다.

'''
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

d = [[0 for _ in range(m)]for _ in range(n)]

#    위  대각선 왼쪽 방향
dx = [-1, -1, 0]
dy = [0, -1, -1]

for i in range(n):
    for j in range(m):
        array = []
        for k in range(3):
            mx = i + dx[k]
            my = j + dy[k]
            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue
            else:
                array.append(d[mx][my])
        if len(array) == 0:
            d[i][j] = board[i][j]
        else:
            d[i][j] = board[i][j] + max(array)

print(d[n-1][m-1])