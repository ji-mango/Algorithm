'''
'안전 영역'
문제 : 재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다. 먼저 어떤 지역의 높이 정보를 파악한다. 
그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다. 이때, 
문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다.
어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오. 

입력 : 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2 이상 100 이하의 정수이다. 
둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 
첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

출력 : 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.

comment : bfs, dfs의 전형적인 알고리즘 문제였다. 이제 bfs, dfs의 풀이방법은 어느정도 숙지가 됐지만, 풀이시간을 단축하기 위한 
노력이 필요한 것 같다.
'''
import sys
import copy
from collections import deque
 
N = int(input())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(j, k, h):
    qX = deque([j])
    qY = deque([k])
    while qX:
        x = qX.popleft()
        y = qY.popleft()
        temp[x][y] = 0
        for g in range(4):
            mx = x + dx[g]
            my = y + dy[g]
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            elif temp[mx][my] != 0 and temp[mx][my] > h:
                temp[mx][my] = 0
                qX.append(mx)
                qY.append(my)
    return
        
result = 0
for i in range(0,max(max(array))+1):
    temp = copy.deepcopy(array)
    count = 0
    for j in range(N):
        for k in range(N):
            if temp[j][k] > i:
                bfs(j, k, i)
                count += 1
    if count > result:
        result = count
print(result)