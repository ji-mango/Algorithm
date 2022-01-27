'''
'인구 이동'

문제 : N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

comment : 너비우선탐색 뿐 아니라 인구 이동 후 평균 인구 수를 구해서 집어넣는다거나, 인구 이동을 할 때 방문기록을 초기화 하는 등
여러가지를 고려해야 해서 어려웠던 문제이다.
'''
from collections import deque
import copy
import sys

N, L, R = map(int, input().split())
people = []
move = []
for i in range(N):
    people.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    move.append([])
    for j in range(N):
        move[i].append(0)
temp = copy.deepcopy(move)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    Xqueue = deque([x])
    Yqueue = deque([y])
    cnt = 1  # 연합 나라 수
    sum = people[x][y]  # 연합 나라 인구 합
    country = [(x,y)]
    move[x][y] = 1
    global end, L, R
    while Xqueue:
        a = Xqueue.popleft()
        b = Yqueue.popleft()
        for i in range(4):
            mx = dx[i] + a
            my = dy[i] + b
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            elif move[mx][my] == 1:
                continue
            elif abs(people[a][b] - people[mx][my]) <= R and abs(people[a][b] - people[mx][my]) >= L:
                sum += people[mx][my]
                cnt += 1
                move[mx][my] = 1
                country.append((mx, my))
                Xqueue.append(mx)
                Yqueue.append(my)
                end += 1
    if cnt != 1:
        avg = sum // cnt
        for i in range(len(country)):
            people[country[i][0]][country[i][1]] = avg


end = 1          # 종료 조건
result = 0
while end != 0:  # 인구 이동할 나라가 없을 경우 종료
    end = 0
    move = copy.deepcopy(temp)
    for i in range(N):
        for j in range(N):
            if move[i][j] == 0:
                bfs(i, j)
    if end != 0:
        result += 1
print(result)

