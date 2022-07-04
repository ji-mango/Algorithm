'''
나무 재테크
'''
'''
# 시간초과
from queue import deque
import sys

n, m, k = map(int, input().split())
temp = []
board = []
tree = deque()

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    temp.append(list(map(int, sys.stdin.readline().split())))
    board.append(list(5 for j in range(n)))


for i in range(m):
    x, y, z = map(int, input().split())
    tree.appendleft([z, x-1, y-1])

def year():
    global n, tree
    dead_tree = []
    new_tree = deque()
    ## 봄
    while len(tree):
        z, x, y = tree.popleft()
        if board[x][y] < z:
            dead_tree.append([z, x, y])
        else:
            board[x][y] -= z
            new_tree.append([z+1, x, y])
    tree = new_tree

    ## 여름
    for i in dead_tree:
        board[i[1]][i[2]] += i[0]//2

    ## 가을
    new_tree = deque()
    while len(tree):
        z, x, y = tree.popleft()
        new_tree.append([z, x, y])
        if z % 5 == 0:
            for i in range(8):
                mx = x + dx[i]
                my = y + dy[i]
                if mx < 0 or mx >= n or my < 0 or my >= n:
                    continue
                else:
                    new_tree.appendleft([1, mx, my])
    tree = new_tree

    ## 겨울
    for i in range(n):
        for j in range(n):
            board[i][j] += temp[i][j]

for i in range(k):
    year()

print(len(tree))
'''

import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
matrix = [[5] * n for _ in range(n)]
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    y, x, age = map(int, input().split())
    tree[y-1][x-1].append(age)

died = deque()
during = deque()
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                length = len(tree[i][j])
                for _ in range(length):
                    level = tree[i][j].pop()
                    if level <= matrix[i][j]:
                        matrix[i][j] -= level
                        level += 1
                        tree[i][j].appendleft(level)
                    else:
                        died.append([i, j, level])

    while died:
        y, x, level = died.pop()
        matrix[y][x] += level // 2

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for t in range(len(tree[i][j])):
                    if tree[i][j][t] % 5 == 0:
                        for q in range(8):
                            dy = i + d[q][0]
                            dx = j + d[q][1]
                            if 0 <= dy < n and 0 <= dx < n:
                                during.append([dy, dx])

    while during:
        du = during.popleft()
        tree[du[0]][du[1]].append(1)

    for i in range(n):
        for j in range(n):
            matrix[i][j] += a[i][j]

result = 0
for i in range(n):
    for j in range(n):
        if tree[i][j]:
            result += len(tree[i][j])

print(result)